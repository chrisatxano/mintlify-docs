# Microservices

## What's possible with Microservices?

* Deploy a custom service right alongside your Xano instance to extend the functionality of what you can do without the data leaving your environment
  * LLMs and AI models _**(GPU-based deployment is available!)**_
  * PDF generation (great for secure data requirements like HIPAA)
  * Media conversion and processing
* Bring a legacy system into the modern age by deploying it inside of a Docker container alongside your Xano instance
* Let separate teams develop specific services to be used in your Xano environment while other developers and product owners work directly inside of Xano

### Microservice Examples and Tutorials

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Unoconv</strong></td><td>Deploy secure file conversation as a part of your Xano environment</td><td><a href="../../.gitbook/assets/unoconv.png">unoconv.png</a></td><td><a href="https://www.youtube.com/watch?v=W2kSIFqzB_4">https://www.youtube.com/watch?v=W2kSIFqzB_4</a></td></tr></tbody></table>

{% hint style="success" %}
The Microservice feature is available as an add-on. Please contact your Xano representative or support for details.&#x20;
{% endhint %}

## Deploying a Microservice

{% stepper %}
{% step %}
### Open the Microservice Management Center

From your instance selection screen, click the :gear: icon and choose Microservices from the panel that opens.
{% endstep %}

{% step %}
### Review your deployment needs before proceeding

#### Deployments

This is where you'll actually deploy your Docker containers

#### Persistent Volumes

If you need persistent storage for one of your microservices, you'll do that here before deployment.

#### Configs

Most microservices will come with a standard configuration. In this section, you can add a customized configuration that better suits your specific needs, if applicable.

You would need to provide a config if you'd like to deploy a Docker image from a private repo.
{% endstep %}

{% step %}
### Add a persistent volume, if necessary.

Click **+Add** under the **Persistent Volumes** section.

**Name:** Provide a descriptive name for your persistent volume. This will help you identify it later.

**Size (Gi):** Please be aware that Xano uses **Gibibytes (Gi)** to denote the size of persistent volumes. A Gibibyte is slightly larger than a Gigabyte (1 GiB = 1024 MiB, while 1 GB = 1000 MB). When planning your storage needs, ensure you are considering the capacity in Gibibytes.

**Type:** Select the type of storage you want to use.

* **SSD (Solid State Drive):** SSD storage offers significantly faster read and write speeds compared to standard storage.
  * **Use Cases:**
    * **Databases:** Ensuring quick query responses and transaction processing.
    * **Caching Layers:** Providing rapid access to frequently used data.
    * **High-IOPS Applications:** Applications that perform a large number of input/output operations.
* **Standard:** Standard storage provides a cost-effective solution for data where fast access speeds are not critical for the application's core functionality.
  * **Use Cases:**
    * **Media Storage:** Storing images, videos, and other large files where retrieval speed is less critical.
    * **Logs:** Archiving application logs.
    * **Backups:** Storing backup data.
    * **Less Frequently Accessed Data:** Data that doesn't require immediate or frequent reads/writes.

**Choosing the Right Storage Type:**

Carefully consider the access patterns and performance requirements of your microservice's data when selecting the storage type. Choosing SSD for performance-sensitive workloads like databases will significantly impact responsiveness. Conversely, using Standard storage for less critical data can help optimize costs.

By configuring persistent volumes, you ensure that your microservice's valuable data persists even if the underlying container or instance is restarted or redeployed.
{% endstep %}

{% step %}
### Add a config file, if necessary.

Click **+Add** under Configs

**Available Config Types and Use Cases:**

The **Type** dropdown offers a variety of options, each suited for different kinds of configuration data:

* **Docker Config:**
  * **Description:** This config type is specifically designed to securely store credentials for private Docker container registries. When your microservice's Docker image is hosted in a private registry, Xano needs the necessary username and password (or access token) to pull the image during deployment.
  * **Use Cases:**
    * **Private Registry Access:** Your organization hosts its Docker images in a private registry on platforms like Docker Hub Private Repositories, Amazon Elastic Container Registry (ECR), Google Container Registry (GCR), or other private registry solutions.
    * **Secure Credential Management:** Avoid embedding registry credentials directly in your deployment scripts or environment variables, which can be less secure. Docker Config provides a centralized and secure way to manage these sensitive details within Xano.
  * **Example:** You have a private Docker Hub repository `myorg/my-app`. To deploy this microservice in Xano, you would create a Docker Config named `dockerhub-credentials` and provide your Docker Hub username and personal access token. Xano will then use these credentials to pull the `myorg/my-app` image during deployment.
* **Text File:**
  * **Description:** A simple way to store plain text configurations. This is useful for basic settings or configuration formats that don't adhere to specific structured formats.
  * **Use Cases:**
    * **Simple Configuration Flags:** Storing basic on/off switches or textual parameters for your application.
    * **License Keys:** Holding software license keys as plain text.
    * **Custom Script Parameters:** Providing arguments to shell scripts executed within your microservice.
  * **Example:** You might have a microservice that reads a `config.txt` file containing a debug flag: `DEBUG=true`. You can store this in a Text File config named `debug-settings`.
* **JSON File:**
  * **Description:** Stores configuration data in the widely used JSON (JavaScript Object Notation) format. This is ideal for structured data that can be easily parsed by most programming languages.
  * **Use Cases:**
    * **API Endpoint Configurations:** Defining base URLs and specific endpoint paths for external APIs your microservice interacts with.
    * **Feature Flags:** Managing the enablement or disablement of specific features within your application.
    * **Database Connection Strings (non-sensitive parts):** Storing parts of database connection strings that are not sensitive credentials.
  *   **Example:** You might have a microservice that needs to connect to a third-party analytics service. You could store the API key and base URL in a JSON config named `analytics-config`:

      ```json
      {
        "api_key": "your_api_key_here",
        "base_url": "[https://api.analytics.com/v1](https://api.analytics.com/v1)"
      }
      ```
* **YAML File:**
  * **Description:** Stores configuration data in YAML, a human-readable data serialization language. Often preferred for its cleaner syntax compared to JSON for more complex configurations.
  * **Use Cases:**
    * **Orchestration Configuration:** Defining how different components of your microservice interact.
    * **Complex Application Settings:** Managing numerous configuration options with hierarchical structures.
    * **Data Pipeline Definitions:** Specifying the steps and parameters for data processing workflows.
  *   **Example:** You might configure logging levels and output formats for your microservice using a YAML config named `logging`:

      ```yaml
      level: INFO
      format: '%(asctime)s - %(levelname)s - %(message)s'
      outputs:
        - type: console
        - type: file
          path: /var/log/app.log
      ```
* **XML File:**
  * **Description:** Stores configuration data in XML. While less common for modern configurations, some legacy systems or specific libraries might still rely on XML.
  * **Use Cases:**
    * **Integration with Legacy Systems:** Configuring interactions with older systems that use XML for configuration.
    * **Specific Library Requirements:** Utilizing libraries within your microservice that expect configuration in XML format.
  * **Example:** Configuring a Java-based application that reads its settings from an `app-config.xml` file.
* **Shell File:**
  * **Description:** Allows you to store and execute shell scripts. This provides a way to automate setup tasks or provide dynamic configurations based on script output.
  * **Use Cases:**
    * **Environment Variable Setup:** Generating and exporting environment variables needed by your microservice.
    * **Initialization Scripts:** Running setup commands or data migrations during microservice startup.
    * **Dynamic Configuration Generation:** Creating configuration files based on external factors or other Configs.
  * **Example:** You could have a `setup.sh` script in a Shell File config that checks for the existence of a directory and creates it if it doesn't exist. The output of this script could then be used by your microservice.
* **HTML File:**
  * **Description:** Stores HTML content. While not typically used for core application configuration, it could be useful for microservices that serve web content or require embedding HTML snippets.
  * **Use Cases:**
    * **Custom Error Pages:** Providing custom HTML for error responses.
    * **Email Templates:** Storing the HTML structure for emails sent by your microservice.
    * **Small Web Content Snippets:** Including static HTML content within your application's responses.
  * **Example:** You might have a microservice that sends out welcome emails. The HTML structure of this email could be stored in an HTML File config named `welcome-email-template`.
* **CSS File:**
  * **Description:** Stores CSS (Cascading Style Sheets) for styling web content served by your microservice.
  * **Use Cases:**
    * **Styling Embedded Web Interfaces:** If your microservice exposes a basic web interface, you can manage its styles using CSS Configs.
    * **Generating Styled Content:** If your microservice generates HTML, you can store the associated styles separately.
  * **Example:** A simple monitoring dashboard exposed by your microservice could have its styles defined in a CSS File config named `dashboard-styles.css`.
* **SCSS File:**
  * **Description:** Stores SCSS, a CSS preprocessor that adds features like variables, nesting, and mixins, making CSS more maintainable and powerful.&#x20;
  * **Use Cases:**
    * **Advanced Web Interface Styling:** For more complex web interfaces or components within your microservice.
    * **Themed Applications:** Managing different visual themes for your microservice's web elements.
  * **Example:** You could define color palettes and reusable style rules in an SCSS File config named `theme.scss`.&#x20;

**Helpers for Adding Configs:**

Xano provides helper buttons to simplify the process of adding certain types of configurations:

* **FROM USER/PASS:** This helper is a shortcut for creating a **Docker Config** by directly prompting you for a username and password.
* **FROM GOOGLE SERVICE ACCOUNT:** This helper assists in configuring access to Google Cloud services containing the necessary service account credentials.
* **FROM AWS:** This helps in configuring access to Amazon Web Services, making it easier to reterieve AWS access keys and secret keys.

By understanding the different Config types and their potential use cases, you can effectively manage your microservice's settings, credentials, and other necessary data within Xano, leading to more robust, secure, and maintainable deployments. Remember to choose the Config type that best suits the format and purpose of your configuration data.
{% endstep %}

{% step %}
### Finally, set up your deployment.

The **Deployment** section is where you define how your microservice, packaged as a Docker image, will be run and managed within Xano. Think of a deployment as the active instance of your microservice.

**Key Concepts:**

* **Docker Image:** The foundational building block of your microservice. It's a standalone package that includes everything needed to run your application: code, runtime, system tools, system libraries, and settings. Docker images can be hosted in public or private repositories.
* **Replicas:** These are the individual running instances of your Docker image. Increasing the number of replicas enhances the availability and scalability of your microservice by distributing incoming requests across multiple instances.
* **Load Balancing:** When you have multiple replicas, Xano automatically distributes incoming API requests across these instances. This ensures that no single instance is overwhelmed and improves the overall performance and resilience of your microservice. Your application should be designed to handle multiple concurrent requests and statelessness to function correctly with replicas.

**Deployment Configuration:**

* **Name:** A unique identifier for this specific microservice deployment within your Xano Function Stack. This name will be used to reference your microservice when building your APIs.
* **Replicas:** Specify the desired number of running instances (replicas) of your Docker image.
  * **Recommendation:** It's often best to start with **1 Replica** while you are initially setting up and testing your microservice. Once it's stable, you can increase the number of replicas for better performance and fault tolerance, if your deployment supports them.
* **Docker Config:** Select the configuration to use for accessing your Docker image repository.
  * **Public Repo:** Choose this if your Docker image is hosted in a public repository (no authentication required).
  * **\<Your Private Config Name>:** If your Docker image is in a private repository, the Docker Configs you've set up in the **Configs** section will appear here. Select the appropriate config containing the necessary credentials to pull the image.
* **Strategy:** Defines how updates to your microservice deployment are handled with minimal downtime.
  * **RollingUpdate:** This strategy gradually updates your replicas. It brings up a new replica with the updated Docker image before taking down an old one. This ensures minimal interruption to your service.
  * **Recreate:** This strategy first takes down all existing replicas and then creates new ones with the updated Docker image. This will result in a period of downtime during the update.

**Containers:**

A deployment can consist of one or more containers. This is useful for running tightly coupled applications that require multiple processes.

* **Name:** A name to identify this specific container within the deployment. This can be the same as the deployment name for single-container deployments or a more specific name for multi-container setups.
* **Type:** Specifies the type of container to run:
  * **Standard:** The primary type for running your main application processes. These containers will run continuously as part of your microservice deployment.
  * **Initialize Only:** This type of container is designed to run a specific task or set of tasks to completion _before_ the Standard containers in the deployment are started. Once the Initialize Only container finishes its execution successfully, it will terminate, and the Standard containers will then be launched.
* **Docker Image:** The URL or identifier of the Docker image to run for this container. This can be a public or private image (authentication for private images is handled at the Deployment level via the "Docker Config").
  * **Multi-Container Example:** Imagine a web application that requires a PHP application server and a PostgreSQL database. You could define two containers within the same deployment: one running the PHP Docker image and another running the PostgreSQL Docker image. These containers can then communicate with each other within the deployment's network.

**Ports:**

This section defines how network traffic is routed to your container(s).

* **+ Add Port:** Click this to define a new port mapping.
* **Container Port:** The port that your application _inside_ the Docker container is listening on. This is defined by how your Docker image is built.
* **Service Port:** The port that Xano's Function Stack will use to expose your microservice externally. When you make an API request to your microservice in Xano, you will target this service port.
  * **Port Mapping:** You can have the Container Port and the Service Port be the same. However, in multi-container deployments, each container that needs to be accessible externally must have a unique Service Port. The Container Port will be specific to the application within each container.

**Environment Variables:**

Environment variables provide a way to configure your containerized application dynamically. These are key-value pairs that can influence the behavior of your application at runtime.

* **+ Add environment variable:** Click this to add a new environment variable.
* **Name:** The name of the environment variable.
* **Value:** The value assigned to the environment variable.
  * **Use Cases:** You can use environment variables to pass database connection details (excluding sensitive credentials, which are better managed with Configs), API keys (for non-critical services), or feature flags to your application.
  * **Best Practice:** For a large number of configuration parameters, especially sensitive ones, consider using **Config Files** instead of environment variables for better organization and security. The specific environment variables your Docker image expects will be documented by the image provider.

**Volumes:**

Volumes provide persistent storage or configuration files to your containers.

* **+ Add volume:** Click this to add a new volume mount.
* **Name:** A name for this volume mount within the deployment.
* **Type:** Specifies the type of volume to mount:
  * **Scratch:** Provides temporary storage that is local to the container instance and is deleted when the container restarts. Useful for ephemeral data like temporary files or caches that don't need to persist.
  * **Persistent Volume:** Mounts a persistent storage volume that you configured in the **Persistent Volumes** section. This is essential for data that needs to survive container restarts and deployments, such as database files or uploaded media.
  * **Config File:** Mounts a configuration file from the **Configs** section into your container.
* **Config:** If you selected "Config File" as the **Type**, this dropdown will appear, allowing you to choose a specific configuration you've created in the **Configs** section.
* **Mount Path:** The path _inside_ the Docker container where the volume or config file will be accessible to your application. This path is determined by how your Docker image is designed to look for these resources.

**Resources:**

This section allows you to define the minimum and maximum CPU and RAM resources that can be allocated to your container(s). You can also specify the number of GPUs (Graphics Processing Units) if your application requires them for tasks like machine learning.

* **Min CPU:** The minimum amount of CPU that will be reserved for each container instance (e.g., 250m represents 0.25 CPU core).
* **Max CPU:** The maximum amount of CPU that each container instance can utilize (e.g., 1000m represents 1 CPU core).
* **Min RAM:** The minimum amount of RAM (memory) that will be reserved for each container instance (e.g., 1024Mi represents 1024 Megabytes).
* **Max RAM:** The maximum amount of RAM that each container instance can utilize (e.g., 2048Mi represents 2048 Megabytes).
* **GPU:** The number of GPUs to allocate to the container (typically used for machine learning workloads).
  * **Resource Management:** Properly configuring resource limits helps ensure that your microservice has the resources it needs to run efficiently and prevents a single microservice from consuming all available resources on the underlying infrastructure.

**Docker Entrypoint Command override:**

This is an advanced setting that allows you to override the default entrypoint command defined in your Docker image. The entrypoint is the first command that runs when a container starts.

* **+ Add command:** Click to specify a new entrypoint command.
  * **Use Case:** You might use this to run a different executable or script as the main process for your container.

**Docker Entrypoint Arguments override:**

This advanced setting allows you to provide arguments to the overridden entrypoint command.

* **+ Add argument:** Click to add an argument for the overridden entrypoint.

**Affinity and Tolerations:**

These are advanced Kubernetes concepts that control how pods (groups of containers) are scheduled onto nodes (servers).

* **Affinity:** Allows you to define rules about which nodes your pods should or should not be placed on based on labels of other nodes or pods.
  * **Use Case:** You might want to ensure that all replicas of a particular microservice are deployed on different nodes for high availability or that certain containers are placed on nodes with specific hardware.
* **Tolerations:** Allow pods to be scheduled onto nodes that have specific taints applied to them. Taints are used to prevent pods from being scheduled onto certain nodes.
  * **Use Case:** If you have specialized nodes (e.g., with GPUs), you might apply a taint to them. Only pods with a corresponding toleration can be scheduled onto these nodes.

These advanced settings provide fine-grained control over the placement and scheduling of your microservice containers within the underlying infrastructure. Understanding these concepts can be beneficial for optimizing resource utilization, ensuring high availability, and meeting specific hardware requirements.
{% endstep %}
{% endstepper %}

### Using a Microservice in the Function Stack

Once deployed, you can interact with the microservice in the Xano Function Stack.

<figure><img src="../../.gitbook/assets/CleanShot 2022-12-28 at 15.58.50.png" alt=""><figcaption></figcaption></figure>

The Microservice function will be similar to an [external API request](../../the-function-stack/functions/apis-and-lambdas/external-api-request.md) function. Although the settings of the function are similar, it's important to call out that the **microservice is all internal traffic, making the interaction secure**.

<figure><img src="../../.gitbook/assets/CleanShot 2022-12-28 at 16.00.37.png" alt=""><figcaption></figcaption></figure>

* **Import Curl** - allows Xano to automatically build the microservice call via a curl command.
* **Host** - Select from a list of your deployments.&#x20;
* **Path** - define the microservice URL path here.
* **Method** - HTTP method just like an API call (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
* **Params** - Any parameters or request body required.
* **Headers** - Define any custom headers.
* **Timeout** - Defines how long the Function Stack will wait in seconds before it considers the Function to be timed out.
* **Follow\_location -** determines if you wish to automatically follow the redirects (if there are any) in the microservice.

For more on Import Curl, Method, Params, Headers, Timeout, and Follow\_location check out the [External API Request](../../the-function-stack/functions/apis-and-lambdas/external-api-request.md) page.

