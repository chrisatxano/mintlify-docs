# Table of contents

* [👋 Welcome to Xano!](README.md)
* [🌟 Frequently Asked Questions](frequently-asked-questions.md)
* [🔐 Security & Compliance (Trust Center)](https://security.xano.com)
* [🙏 Feature Requests](https://community.xano.com/feature-requests)
* [💔 Known Issues](https://community.xano.com/known-issues)

## Before You Begin

* [Using These Docs](before-you-begin/using-these-docs.md)
* [Where should I start?](before-you-begin/where-should-i-start.md)
* [Set Up a Free Xano Account](before-you-begin/set-up-a-free-xano-account.md)
* [Key Concepts](before-you-begin/key-concepts.md)
* [The Development Life Cycle](before-you-begin/the-development-life-cycle.md)
* [Navigating Xano](before-you-begin/navigating-xano.md)
* [Plans & Pricing](https://www.xano.com/pricing/)

## The Database

* [Designing your Database](the-database/designing-your-database.md)
* [Database Basics](the-database/database-basics/README.md)
  * [Using the Xano Database](the-database/database-basics/using-the-xano-database.md)
  * [Field Types](the-database/database-basics/field-types.md)
  * [Relationships](the-database/database-basics/relationships.md)
  * [Database Views](the-database/database-basics/database-views.md)
  * [Export and Sharing](the-database/database-basics/export-and-sharing.md)
  * [Data Sources](the-database/database-basics/data-sources.md)
* [Migrating your Data](the-database/migrating-your-data/README.md)
  * [Bubble to Xano](the-database/migrating-your-data/bubble-to-xano.md)
  * [Airtable to Xano](the-database/migrating-your-data/airtable-to-xano.md)
  * [Supabase to Xano](the-database/migrating-your-data/supabase-to-xano.md)
  * [Fastgen to Xano](the-database/migrating-your-data/fastgen-to-xano.md)
  * [Adalo to Xano](the-database/migrating-your-data/adalo-to-xano.md)
  * [Google Sheets to Xano](the-database/migrating-your-data/google-sheets-to-xano.md)
  * [CSV Import & Export](the-database/migrating-your-data/csv-import-and-export.md)
  * [Add via API](the-database/migrating-your-data/add-via-api.md)
  * [Connect to an External Database](the-database/migrating-your-data/connect-to-an-external-database.md)
* [Database Performance and Maintenance](the-database/database-performance-and-maintenance/README.md)
  * [Storage](the-database/database-performance-and-maintenance/storage.md)
  * [Indexing](the-database/database-performance-and-maintenance/indexing.md)
  * [Maintenance](the-database/database-performance-and-maintenance/maintenance.md)
  * [Schema Versioning](the-database/database-performance-and-maintenance/schema-versioning.md)

## 🛠️ The Function Stack

* [Building with Visual Development](the-function-stack/building-with-visual-development/README.md)
  * [APIs](the-function-stack/building-with-visual-development/apis/README.md)
    * [Swagger (OpenAPI Documentation)](the-function-stack/building-with-visual-development/apis/swagger-openapi-documentation.md)
  * [Custom Functions](the-function-stack/building-with-visual-development/custom-functions/README.md)
    * [Async Functions](the-function-stack/building-with-visual-development/custom-functions/async-functions.md)
  * [Background Tasks](the-function-stack/building-with-visual-development/background-tasks.md)
  * [Triggers](the-function-stack/building-with-visual-development/triggers.md)
  * [Middleware](the-function-stack/building-with-visual-development/middleware.md)
  * [Configuring Expressions](the-function-stack/building-with-visual-development/configuring-expressions.md)
  * [Working with Data](the-function-stack/building-with-visual-development/working-with-data.md)
* [Functions](the-function-stack/functions/README.md)
  * [AI Tools](the-function-stack/functions/ai-tools.md)
  * [Database Requests](the-function-stack/functions/database-requests/README.md)
    * [Query All Records](the-function-stack/functions/database-requests/query-all-records/README.md)
      * [External Filtering Examples](the-function-stack/functions/database-requests/query-all-records/external-filtering-examples.md)
    * [Get Record](the-function-stack/functions/database-requests/get-record.md)
    * [Add Record](the-function-stack/functions/database-requests/add-record.md)
    * [Edit Record](the-function-stack/functions/database-requests/edit-record.md)
    * [Add or Edit Record](the-function-stack/functions/database-requests/add-or-edit-record.md)
    * [Patch Record](the-function-stack/functions/database-requests/patch-record.md)
    * [Delete Record](the-function-stack/functions/database-requests/delete-record.md)
    * [Bulk Operations](the-function-stack/functions/database-requests/bulk-operations.md)
    * [Database Transaction](the-function-stack/functions/database-requests/database-transaction.md)
    * [External Database Query](the-function-stack/functions/database-requests/external-database-query.md)
    * [Direct Database Query](the-function-stack/functions/database-requests/direct-database-query.md)
    * [Get Database Schema](the-function-stack/functions/database-requests/get-database-schema.md)
  * [Data Manipulation](the-function-stack/functions/data-manipulation/README.md)
    * [Create Variable](the-function-stack/functions/data-manipulation/create-variable.md)
    * [Update Variable](the-function-stack/functions/data-manipulation/update-variable.md)
    * [Conditional](the-function-stack/functions/data-manipulation/conditional.md)
    * [Switch](the-function-stack/functions/data-manipulation/switch.md)
    * [Loops](the-function-stack/functions/data-manipulation/loops.md)
    * [Math](the-function-stack/functions/data-manipulation/math.md)
    * [Arrays](the-function-stack/functions/data-manipulation/arrays.md)
    * [Objects](the-function-stack/functions/data-manipulation/objects.md)
    * [Text](the-function-stack/functions/data-manipulation/text.md)
  * [Security](the-function-stack/functions/security.md)
  * [APIs & Lambdas](the-function-stack/functions/apis-and-lambdas/README.md)
    * [Realtime Functions](the-function-stack/functions/apis-and-lambdas/realtime-functions.md)
    * [External API Request](the-function-stack/functions/apis-and-lambdas/external-api-request.md)
    * [Lambda Functions](the-function-stack/functions/apis-and-lambdas/lambda-functions.md)
      * [Supported Libraries](the-function-stack/functions/apis-and-lambdas/lambda-functions/supported-libraries.md)
  * [Data Caching (Redis)](the-function-stack/functions/data-caching-redis.md)
  * [Custom Functions](the-function-stack/functions/custom-functions.md)
  * [Utility Functions](the-function-stack/functions/utility-functions.md)
  * [File Storage](the-function-stack/functions/file-storage.md)
  * [Cloud Services](the-function-stack/functions/cloud-services.md)
  * [Connected](the-function-stack/functions/connected.md)
* [Filters](the-function-stack/filters/README.md)
  * [Manipulation](the-function-stack/filters/manipulation.md)
  * [Math](the-function-stack/filters/math.md)
  * [Timestamp](the-function-stack/filters/timestamp.md)
  * [Text](the-function-stack/filters/text.md)
  * [Array](the-function-stack/filters/array.md)
  * [Transform](the-function-stack/filters/transform.md)
  * [Conversion](the-function-stack/filters/conversion.md)
  * [Comparison](the-function-stack/filters/comparison.md)
  * [Security](the-function-stack/filters/security.md)
* [Data Types](the-function-stack/data-types/README.md)
  * [Text](the-function-stack/data-types/text.md)
  * [Expression](the-function-stack/data-types/expression.md)
  * [Array](the-function-stack/data-types/array.md)
  * [Object](the-function-stack/data-types/object.md)
  * [Integer](the-function-stack/data-types/integer.md)
  * [Decimal](the-function-stack/data-types/decimal.md)
  * [Boolean](the-function-stack/data-types/boolean.md)
  * [Timestamp](the-function-stack/data-types/timestamp.md)
  * [Null](the-function-stack/data-types/null.md)
* [Environment Variables](the-function-stack/environment-variables.md)
* [Additional Features](the-function-stack/additional-features/README.md)
  * [Response Caching](the-function-stack/additional-features/response-caching.md)

## Testing and Debugging <a href="#testing-debugging" id="testing-debugging"></a>

* [Testing and Debugging Function Stacks](testing-debugging/testing-and-debugging-function-stacks.md)
* [Unit Tests](testing-debugging/unit-tests.md)
* [Test Suites](testing-debugging/test-suites.md)

## File Storage

* [File Storage in Xano](file-storage/file-storage-in-xano.md)
* [Private File Storage](file-storage/private-file-storage.md)

## Realtime

* [Realtime in Xano](realtime/realtime-in-xano.md)
* [Channel Permissions](realtime/channel-permissions.md)
* [Realtime in Webflow](realtime/realtime-in-webflow.md)

## Maintenance, Monitoring, and Logging

* [Statement Explorer](maintenance-monitoring-and-logging/statement-explorer.md)
* [Request History](maintenance-monitoring-and-logging/request-history.md)
* [Instance Dashboard](maintenance-monitoring-and-logging/instance-dashboard/README.md)
  * [Memory Usage](maintenance-monitoring-and-logging/instance-dashboard/memory-usage.md)

## Building Backend Features

* [User Authentication & User Data](building-backend-features/user-authentication-and-user-data/README.md)
  * [Separating User Data](building-backend-features/user-authentication-and-user-data/separating-user-data.md)
  * [Restricting Access (RBAC)](building-backend-features/user-authentication-and-user-data/restricting-access-rbac.md)
  * [OAuth (SSO)](building-backend-features/user-authentication-and-user-data/oauth-sso.md)
* [Payments](building-backend-features/payments.md)
* [Webhooks](building-backend-features/webhooks.md)
* [Notifications](building-backend-features/notifications.md)
* [Messaging](building-backend-features/messaging.md)
* [Emails](building-backend-features/emails.md)
* [Location Data](building-backend-features/location-data.md)
* [User Roles](building-backend-features/user-roles.md)
* [Connecting to External Systems & Services](building-backend-features/connecting-to-external-systems-and-services.md)
* [Custom Report Generation](building-backend-features/custom-report-generation.md)
* [Fuzzy Search](building-backend-features/fuzzy-search.md)
* [Chatbots](building-backend-features/chatbots.md)

## Connecting to a Front-end

* [Fundamentals](connecting-to-a-front-end/fundamentals.md)
* [Adalo](connecting-to-a-front-end/adalo.md)
* [Appgyver](connecting-to-a-front-end/appgyver.md)
* [Bubble](connecting-to-a-front-end/bubble.md)
* [Flutterflow](connecting-to-a-front-end/flutterflow.md)
* [Javascript](connecting-to-a-front-end/javascript.md)
* [Toddle](connecting-to-a-front-end/toddle.md)
* [WeWeb](connecting-to-a-front-end/weweb.md)
* [Webflow](connecting-to-a-front-end/webflow.md)

## Xano Features

* [Snippets](xano-features/snippets.md)
* [Instance Settings](xano-features/instance-settings/README.md)
  * [Release Track Preferences](xano-features/instance-settings/release-track-preferences.md)
  * [Static IP (Outgoing)](xano-features/instance-settings/static-ip-outgoing.md)
  * [Change Server Region](xano-features/instance-settings/change-server-region.md)
  * [Direct Database Connector](xano-features/instance-settings/direct-database-connector.md)
  * [Backup and Restore](xano-features/instance-settings/backup-and-restore.md)
  * [Security Policy](xano-features/instance-settings/security-policy.md)
* [Advanced Back-end Features](xano-features/advanced-back-end-features/README.md)
  * [Xano Link](xano-features/advanced-back-end-features/xano-link.md)
  * [Developer API (Deprecated)](xano-features/advanced-back-end-features/developer-api-deprecated.md)
* [Metadata API](xano-features/metadata-api/README.md)
  * [Master Metadata API](xano-features/metadata-api/master-metadata-api.md)
  * [Tables and Schema](xano-features/metadata-api/tables-and-schema.md)
  * [Content](xano-features/metadata-api/content.md)
  * [Search](xano-features/metadata-api/search.md)
  * [File](xano-features/metadata-api/file.md)
  * [Request History](xano-features/metadata-api/request-history.md)
  * [Workspace Import and Export](xano-features/metadata-api/workspace-import-and-export.md)
  * [Token Scopes Reference](xano-features/metadata-api/token-scopes-reference.md)

## Xano AI

* [Building a Backend Using AI](xano-ai/building-a-backend-using-ai.md)
* [Get Started Assistant](xano-ai/get-started-assistant.md)
* [AI Database Assistant](xano-ai/ai-database-assistant.md)
* [AI Lambda Assistant](xano-ai/ai-lambda-assistant.md)
* [AI SQL Assistant](xano-ai/ai-sql-assistant.md)
* [API Request Assistant](xano-ai/api-request-assistant.md)
* [Template Engine](xano-ai/template-engine.md)
* [Streaming APIs](xano-ai/streaming-apis.md)

## AI Tools

* [MCP Servers](ai-tools/mcp-servers/README.md)
  * [Connecting Clients](ai-tools/mcp-servers/connecting-clients.md)
  * [MCP Functions](ai-tools/mcp-servers/mcp-functions.md)

## Xano Transform

* [Using Xano Transform](xano-transform/using-xano-transform.md)

## Xano Actions

* [What are Actions?](xano-actions/what-are-actions.md)
* [Browse Actions](https://xano.com/actions)

## Team Collaboration

* [Realtime Collaboration](team-collaboration/realtime-collaboration.md)
* [Managing Team Members](team-collaboration/managing-team-members.md)
* [Branching & Merging](team-collaboration/branching-and-merging.md)
* [Role-based Access Control (RBAC)](team-collaboration/role-based-access-control-rbac.md)

## Agencies

* [Xano for Agencies](agencies/xano-for-agencies.md)
* [Agency Features](agencies/agency-features/README.md)
  * [Agency Dashboard](agencies/agency-features/agency-dashboard.md)
  * [Client Invite](agencies/agency-features/client-invite.md)
  * [Transfer Ownership](agencies/agency-features/transfer-ownership.md)
  * [Agency Profile](agencies/agency-features/agency-profile.md)
  * [Commission](agencies/agency-features/commission.md)
  * [Private Marketplace](agencies/agency-features/private-marketplace.md)

## Enterprise

* [Xano for Enterprise](enterprise/xano-for-enterprise.md)
* [Enterprise Features](enterprise/enterprise-features/README.md)
  * [Microservices](enterprise/enterprise-features/microservices.md)
  * [Tenant Center](enterprise/enterprise-features/tenant-center.md)
  * [Compliance Center](enterprise/enterprise-features/compliance-center.md)
  * [Security Policy](enterprise/enterprise-features/security-policy.md)
  * [Instance Activity](enterprise/enterprise-features/instance-activity.md)
  * [Deployment](enterprise/enterprise-features/deployment.md)
  * [RBAC (Role-based Access Control)](enterprise/enterprise-features/rbac-role-based-access-control.md)
  * [Xano Link](enterprise/enterprise-features/xano-link.md)

## Your Xano Account

* [Account Page](your-xano-account/account-page.md)
* [Billing](your-xano-account/billing.md)
* [Referrals & Commissions](your-xano-account/referrals-and-commissions.md)

## Troubleshooting & Support

* [Error Reference](troubleshooting-and-support/error-reference.md)
* [Troubleshooting Performance](troubleshooting-and-support/troubleshooting-performance/README.md)
  * [When a single workflow feels slow](troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow.md)
  * [When everything feels slow](troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow.md)
  * [RAM Usage](troubleshooting-and-support/troubleshooting-performance/ram-usage.md)
  * [Function Stack Performance](troubleshooting-and-support/troubleshooting-performance/function-stack-performance.md)
* [Getting Help](troubleshooting-and-support/getting-help/README.md)
  * [Granting Access](troubleshooting-and-support/getting-help/granting-access.md)
  * [Community Code of Conduct](troubleshooting-and-support/getting-help/community-code-of-conduct.md)
  * [Community Content Modification Policy](troubleshooting-and-support/getting-help/community-content-modification-policy.md)

***

* [Developer API (Deprecated)](developer-api-deprecated.md)
* [Adjust Server Performance](adjust-server-performance.md)

## Special Pricing <a href="#special-discount-pricing" id="special-discount-pricing"></a>

* [Students & Education](special-discount-pricing/students.md)
* [Non-Profits](special-discount-pricing/non-profits.md)

***

* [Increasing Plan Limits](increasing-plan-limits.md)
* [API Rate Limit](api-rate-limit.md)
* [Tool Rate Limit](tool-rate-limit.md)

## Security

* [Best Practices](security/best-practices.md)

***

* [instances](instances/README.md)
  * [API Rate Limit](instances/api-rate-limit.md)

## Xanoscript

* [Introduction to XanoScript](xanoscript/introduction-to-xanoscript.md)
* [XanoScript Key Concepts](xanoscript/keyconcepts.md)
* [XanoScript for the Database](xanoscript/db/README.md)
  * [Field Type Reference](xanoscript/db/field-type-reference.md)
* [XanoScript for Function Stacks](xanoscript/fs/README.md)
  * [Input Types Reference](xanoscript/fs/input-types-reference.md)
  * [Function Reference](xanoscript/fs/function-reference/README.md)
    * [Database Operations](xanoscript/fs/function-reference/database-operations.md)
    * [Data Manipulation](xanoscript/fs/function-reference/data-manipulation/README.md)
      * [Loops](xanoscript/fs/function-reference/data-manipulation/loops.md)
      * [Math](xanoscript/fs/function-reference/data-manipulation/math.md)
      * [Arrays](xanoscript/fs/function-reference/data-manipulation/arrays.md)
      * [Objects](xanoscript/fs/function-reference/data-manipulation/objects.md)
      * [Text](xanoscript/fs/function-reference/data-manipulation/text.md)
      * [Variables](xanoscript/fs/function-reference/data-manipulation/variables.md)
      * [Conditionals](xanoscript/fs/function-reference/data-manipulation/conditionals.md)
    * [Security](xanoscript/fs/function-reference/security.md)
    * [APIs & Lambdas](xanoscript/fs/function-reference/apis-and-lambdas.md)
    * [Data Caching (Redis)](xanoscript/fs/function-reference/data-caching-redis.md)
    * [Custom Functions](xanoscript/fs/function-reference/custom-functions.md)
    * [Utility Functions](xanoscript/fs/function-reference/utility-functions.md)
    * [File Storage](xanoscript/fs/function-reference/file-storage.md)
    * [Cloud Services](xanoscript/fs/function-reference/cloud-services/README.md)
      * [AWS OpenSearch](xanoscript/fs/function-reference/cloud-services/aws-opensearch.md)
      * [AWS S3](xanoscript/fs/function-reference/cloud-services/aws-s3.md)
      * [Azure Blob Storage](xanoscript/fs/function-reference/cloud-services/azure-blob-storage.md)
      * [Google Cloud Storage](xanoscript/fs/function-reference/cloud-services/google-cloud-storage.md)
      * [Elasticsearch](xanoscript/fs/function-reference/cloud-services/elasticsearch.md)
      * [Algolia](xanoscript/fs/function-reference/cloud-services/algolia.md)
  * [Filter Reference](xanoscript/fs/filter-reference/README.md)
    * [Manipulation](xanoscript/fs/filter-reference/manipulation.md)
    * [Math](xanoscript/fs/filter-reference/math.md)
    * [Timestamp](xanoscript/fs/filter-reference/timestamp.md)
    * [Text](xanoscript/fs/filter-reference/text.md)
    * [Array](xanoscript/fs/filter-reference/array.md)
    * [Transform](xanoscript/fs/filter-reference/transform.md)
    * [Comparison](xanoscript/fs/filter-reference/comparison.md)
    * [Security](xanoscript/fs/filter-reference/security.md)
* [XanoScript for Background Tasks](xanoscript/ts.md)
