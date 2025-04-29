import os
import re
import shutil

def rename_md_to_mdx_in_dir(directory):
    """Renames all .md files to .mdx within a directory and its subdirectories."""
    if not os.path.isdir(directory):
        print(f"Warning: Directory not found for renaming: '{directory}'")
        return

    print(f"Renaming .md to .mdx in '{directory}'...")
    renamed_count = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.md'):
                old_filepath = os.path.join(dirpath, filename)
                # Ensure original extension was .md before adding .x
                if old_filepath.lower().endswith('.md'):
                     new_filepath = old_filepath[:-3] + '.mdx'
                     try:
                         os.rename(old_filepath, new_filepath)
                         renamed_count += 1
                         # print(f"Renamed: {filename} -> {os.path.basename(new_filepath)}") # Optional: noisy
                     except Exception as e:
                         print(f"Error renaming file {old_filepath}: {e}")
    print(f"Renamed {renamed_count} .md files to .mdx in '{directory}'.")


def move_gitbook_assets_and_includes(root_dir):
    """
    Moves Gitbook includes and assets to their new locations.
    Preserves internal directory structure and renames includes to .mdx.
    """
    old_includes_dir = os.path.join(root_dir, '.gitbook', 'includes')
    new_snippets_dir = os.path.join(root_dir, 'snippets')
    old_assets_dir = os.path.join(root_dir, '.gitbook', 'assets')
    new_assets_dir = os.path.join(root_dir, 'assets')

    # --- Move Includes/Snippets and Rename to .mdx ---
    if os.path.exists(old_includes_dir):
        print(f"Moving includes from '{old_includes_dir}' to '{new_snippets_dir}' and renaming .md to .mdx...")
        try:
            # Walk the source directory
            for dirpath, dirnames, filenames in os.walk(old_includes_dir):
                # Calculate the corresponding destination directory path
                relative_path = os.path.relpath(dirpath, old_includes_dir)
                dest_dir = os.path.join(new_snippets_dir, relative_path)

                # Create destination directory if it doesn't exist
                os.makedirs(dest_dir, exist_ok=True)

                # Move and rename files
                for filename in filenames:
                    old_filepath = os.path.join(dirpath, filename)
                    # Determine the new filename (rename .md to .mdx)
                    new_filename = filename
                    if filename.lower().endswith('.md'):
                        new_filename = filename[:-3] + '.mdx' # Simple replace for .md
                    # Ensure no double .mdx if original was e.g. .md.md
                    if new_filename.lower().endswith('.md.mdx'):
                         new_filename = new_filename[:-7] + '.mdx'

                    new_filepath = os.path.join(dest_dir, new_filename)

                    # Move the file
                    shutil.move(old_filepath, new_filepath)
                    # print(f"Moved & Renamed: {old_filepath} -> {new_filepath}") # Optional: noisy

            # After moving contents, remove the original includes directory
            shutil.rmtree(old_includes_dir)
            print("Includes moved and renamed successfully.")
        except Exception as e:
            print(f"Error moving/renaming includes: {e}")
    else:
        print(f"Old includes directory not found: '{old_includes_dir}'. Skipping.")

    # --- Move Assets ---
    if os.path.exists(old_assets_dir):
        print(f"Moving assets from '{old_assets_dir}' to '{new_assets_dir}'...")
        try:
            if not os.path.exists(new_assets_dir):
                shutil.copytree(old_assets_dir, new_assets_dir)
            else:
                # If dest exists, walk source and move individual files/dirs (merging)
                for item in os.listdir(old_assets_dir):
                     s = os.path.join(old_assets_dir, item)
                     d = os.path.join(new_assets_dir, item)
                     if os.path.isdir(s):
                         if os.path.exists(d):
                              # Use copytree with dirs_exist_ok=True for merging
                              shutil.copytree(s, d, dirs_exist_ok=True)
                              shutil.rmtree(s) # Remove source after successful merge copy
                         else:
                             shutil.move(s, d) # Move directory if destination doesn't exist
                     else:
                         shutil.move(s, d) # Move file

            # After moving contents, remove the original assets directory
            if os.path.exists(old_assets_dir): # Check again in case it was already gone
                 shutil.rmtree(old_assets_dir)
            print("Assets moved successfully.")
        except Exception as e:
             print(f"Error moving assets: {e}")
    else:
        print(f"Old assets directory not found: '{old_assets_dir}'. Skipping.")


def update_link_extension(match):
    """Helper function for re.sub to update .md links to .mdx."""
    link_path = match.group(1)

    # Ignore external links, anchors, mailto etc.
    if re.match(r'^[a-zA-Z]+:', link_path) or link_path.startswith('#'):
        return link_path

    # If it ends with .md (case-insensitive), change to .mdx
    if link_path.lower().endswith('.md'):
        # Simple replace .md with .mdx
        # Need to handle potential query parameters or anchors correctly
        parts = re.split(r'([?#])', link_path, 1) # Split at first ? or #
        base_path = parts[0]
        suffix = ''.join(parts[1:]) # Keep query/anchor if any

        # Ensure original extension was .md before adding .x
        if base_path.lower().endswith('.md'):
            return base_path[:-3] + '.mdx' + suffix
        else:
             return link_path # Did not end in .md

    # If it doesn't end with .md, return as is
    return link_path


def process_markdown_file(filepath):
    """
    Reads a markdown file, applies transformations (except final rename),
    and returns the modified content.
    """
    # print(f"Processing content of: {filepath}") # Optional: noisy
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        modified_content = content

        # 1. Replace Includes
        # Finds {% include ".gitbook/includes/some/path/file.md" %}
        # Replaces with <Snippet file="some/path/file.mdx" />
        # Using re.sub with a function to handle the captured path correctly
        def replace_include_path(match):
            gitbook_path = match.group(1)
            # Remove the '.gitbook/includes/' prefix
            relative_path = gitbook_path.replace('.gitbook/includes/', '', 1)
            # Ensure the include file extension is .mdx in the new syntax
            if relative_path.lower().endswith('.md'):
                 relative_path = relative_path[:-3] + '.mdx'
                 # Ensure no double .mdx if original was e.g. .md.md
                 if relative_path.lower().endswith('.md.mdx'):
                      relative_path = relative_path[:-7] + '.mdx'

            return f'<Snippet file="{relative_path}" />'

        # Updated regex to capture path after .gitbook/includes/
        modified_content = re.sub(
            r'{% include ["\']\.gitbook/includes/(.*?)["\'] %}',
            replace_include_path,
            modified_content
        )

        # 2. Handle Titles
        # Find the first line that is an H1 and is not part of YAML frontmatter
        lines = modified_content.splitlines()
        new_lines = []
        in_frontmatter = False
        title_replaced = False

        # Check for YAML frontmatter
        if lines and lines[0].strip() == '---':
            in_frontmatter = True
            new_lines.append(lines[0]) # Add the first ---

        for i, line in enumerate(lines):
            if in_frontmatter:
                new_lines.append(line)
                if line.strip() == '---' and i > 0: # End of frontmatter (check i>0 to avoid empty file issues)
                    in_frontmatter = False
                continue # Skip title check while in frontmatter

            if not title_replaced:
                # Check if it's the first non-frontmatter line starting with #
                # Allow for leading whitespace before #
                title_match = re.match(r'^(\s*#\s*)(.+)', line)
                if title_match:
                    # Extract the title text (group 2) and the prefix (group 1)
                    prefix = title_match.group(1)
                    title_text = title_match.group(2).strip() # Trim whitespace from title text
                    new_lines.append(f"{prefix}'{title_text}'") # Wrap title text in single quotes
                    title_replaced = True # Only replace the first H1
                    continue # Move to the next line

            # If line is not frontmatter and not the title line we replaced, add it as is
            new_lines.append(line)

        modified_content = '\n'.join(new_lines)


        # 3. Replace Hint Blocks
        # Mapping Gitbook styles to Mintlify component names
        hint_component_map = {
            "info": "Info",
            "warning": "Warning",
            "danger": "Danger",
            "success": "Success",
            # Add other Gitbook styles if needed and map to a default or specific component
            # default maps to Info based on assumption
        }

        # Regex to find the entire hint block, including the content
        # re.DOTALL allows . to match newlines
        # (.*?) is non-greedy match for style
        # (.*?) is non-greedy match for content
        hint_regex = r'{% hint style=["\'](.*?)["\'] %}(.*?){% endhint %}'

        def replace_hint_block(match):
            style = match.group(1).lower() # Get the style and make it lowercase
            content = match.group(2).strip() # Get the content and trim whitespace
            component_name = hint_component_map.get(style, "Info") # Get component name, default to Info
            return f"<{component_name}>\n\n{content}\n\n</{component_name}>" # Format as component

        modified_content = re.sub(hint_regex, replace_hint_block, modified_content, flags=re.DOTALL)

        # 4. Update Image Paths
        # Find <img> tags with src attributes
        # Regex finds <img... src="..." ...> or <img... src='...' ...>
        # Captures the content of the src attribute
        img_regex = r'<img.*?src=["\'](.*?)["\'].*?>'

        def update_img_src(match):
            full_img_tag = match.group(0) # The entire <img> tag
            src_path = match.group(1)    # The value of the src attribute

            # Check if the path looks like a Gitbook asset path
            if '.gitbook/assets/' in src_path:
                 # Replace the Gitbook part with the new Mintlify assets path
                # Using a simple replace assumes /assets/ is the correct base path from root
                new_src_path = src_path.replace('.gitbook/assets/', '/assets/')
                # Replace the original src attribute value within the captured tag
                # This is safer than just string replacing in modified_content
                updated_img_tag = re.sub(
                    r'src=["\'].*?["\']', # Find the src attribute again within the tag
                    f'src="{new_src_path}"', # Replace with the new path (using double quotes)
                    full_img_tag
                )
                # Handle potential single quotes in original src if the above didn't
                updated_img_tag = updated_img_tag.replace("src='", 'src="').replace("'", '"')
                return updated_img_tag
            else:
                # If it doesn't look like a Gitbook asset, return the original tag
                return full_img_tag

        modified_content = re.sub(img_regex, update_img_src, modified_content)

        # 5. Update Internal Links (.md to .mdx)
        # Find Markdown links [text](path)
        markdown_link_regex = r'\[.*?\]\((.*?)\)'
        # Find HTML links <a href="path">
        html_link_regex = r'<a.*?href=["\'](.*?)["\'].*?>' # Captures href content

        # Apply the update_link_extension function to both types of links
        modified_content = re.sub(markdown_link_regex, lambda m: f'[{m.group(0).split("]")[0]}]({update_link_extension(m)})', modified_content)
        # For HTML links, need to reconstruct the tag carefully
        def update_html_href(match):
            full_tag = match.group(0)
            href_value = match.group(1)
            new_href_value = update_link_extension(match) # Use the helper function
            # Replace the original href value within the tag
            # Be careful with single vs double quotes
            if f'href="{href_value}"' in full_tag:
                 return full_tag.replace(f'href="{href_value}"', f'href="{new_href_value}"')
            elif f"href='{href_value}'" in full_tag:
                 return full_tag.replace(f"href='{href_value}'", f"href='{new_href_value}'")
            else:
                 return full_tag # Should not happen if regex matched correctly

        modified_content = re.sub(html_link_regex, update_html_href, modified_content, flags=re.DOTALL | re.IGNORECASE) # Case insensitive for tag/attribute names


        return modified_content

    except Exception as e:
        print(f"Error reading/processing {filepath}: {e}")
        return None # Indicate failure

def main(root_documentation_dir):
    """
    Main function to orchestrate the migration process.
    """
    if not os.path.isdir(root_documentation_dir):
        print(f"Error: Directory not found at '{root_documentation_dir}'")
        return

    print(f"Starting migration process for documentation in '{root_documentation_dir}'")

    # Step 1: Move assets and includes (and rename includes to .mdx)
    move_gitbook_assets_and_includes(root_documentation_dir)

    # Step 2, 3, 4, 5 & 6: Traverse, process content, write, and rename main files
    print("\nProcessing and renaming markdown files...")
    processed_count = 0
    renamed_count = 0
    skipped_count = 0

    # First, find all .md files
    md_files_to_process = []
    for dirpath, _, filenames in os.walk(root_documentation_dir):
        for filename in filenames:
            if filename.lower().endswith('.md'):
                filepath = os.path.join(dirpath, filename)
                md_files_to_process.append(filepath)

    # Process each found .md file
    for filepath in md_files_to_process:
        if not os.path.exists(filepath):
             print(f"Warning: File disappeared during processing loop: {filepath}. Skipping.")
             skipped_count += 1
             continue

        modified_content = process_markdown_file(filepath)

        if modified_content is not None:
            try:
                # Write the modified content back to the original file path first
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified_content)

                processed_count += 1

                # Now rename the file to .mdx
                if filepath.lower().endswith('.md'): # Ensure it still ends with .md before renaming
                    new_filepath = filepath[:-3] + '.mdx'
                    # Ensure no double .mdx if original was e.g. .md.md
                    if new_filepath.lower().endswith('.md.mdx'):
                         new_filepath = new_filepath[:-7] + '.mdx'

                    os.rename(filepath, new_filepath)
                    renamed_count += 1
                    print(f"Processed and Renamed: {os.path.basename(filepath)} -> {os.path.basename(new_filepath)}")
                else:
                    # This case should ideally not happen if md_files_to_process was built correctly
                    print(f"Warning: File {filepath} did not end in .md after processing. Not renamed.")
            except Exception as e:
                print(f"Error writing or renaming {filepath}: {e}")
                skipped_count += 1
        else:
             skipped_count += 1 # Error during processing

    print(f"\nMigration complete.")
    print(f"Processed content of {processed_count} files.")
    print(f"Renamed {renamed_count} .md files to .mdx.")
    print(f"Skipped {skipped_count} files due to errors or unexpected state.")


if __name__ == "__main__":
    # Get the root documentation directory from user input
    doc_root = input("Enter the path to the root of your Gitbook documentation folder: ")

    # Add a confirmation step
    confirm = input(f"This script will modify files and move directories within '{doc_root}'. Have you backed up your data? (yes/no): ").lower()

    if confirm == 'yes':
        main(doc_root)
    else:
        print("Migration cancelled by user.")
        print("Please back up your data before running the script.")