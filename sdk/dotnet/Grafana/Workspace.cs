// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Grafana
{
    /// <summary>
    /// Definition of AWS::Grafana::Workspace Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:grafana:Workspace")]
    public partial class Workspace : global::Pulumi.CustomResource
    {
        [Output("accountAccessType")]
        public Output<Pulumi.AwsNative.Grafana.WorkspaceAccountAccessType?> AccountAccessType { get; private set; } = null!;

        /// <summary>
        /// List of authentication providers to enable.
        /// </summary>
        [Output("authenticationProviders")]
        public Output<ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceAuthenticationProviderTypes>> AuthenticationProviders { get; private set; } = null!;

        /// <summary>
        /// A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
        /// </summary>
        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        /// <summary>
        /// Timestamp when the workspace was created.
        /// </summary>
        [Output("creationTimestamp")]
        public Output<string> CreationTimestamp { get; private set; } = null!;

        /// <summary>
        /// List of data sources on the service managed IAM role.
        /// </summary>
        [Output("dataSources")]
        public Output<ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceDataSourceType>> DataSources { get; private set; } = null!;

        /// <summary>
        /// Description of a workspace.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Endpoint for the Grafana workspace.
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// Version of Grafana the workspace is currently using.
        /// </summary>
        [Output("grafanaVersion")]
        public Output<string> GrafanaVersion { get; private set; } = null!;

        /// <summary>
        /// Timestamp when the workspace was last modified
        /// </summary>
        [Output("modificationTimestamp")]
        public Output<string> ModificationTimestamp { get; private set; } = null!;

        /// <summary>
        /// The user friendly name of a workspace.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        /// </summary>
        [Output("notificationDestinations")]
        public Output<ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceNotificationDestinationType>> NotificationDestinations { get; private set; } = null!;

        /// <summary>
        /// The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        /// </summary>
        [Output("organizationRoleName")]
        public Output<string?> OrganizationRoleName { get; private set; } = null!;

        /// <summary>
        /// List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        /// </summary>
        [Output("organizationalUnits")]
        public Output<ImmutableArray<string>> OrganizationalUnits { get; private set; } = null!;

        [Output("permissionType")]
        public Output<Pulumi.AwsNative.Grafana.WorkspacePermissionType?> PermissionType { get; private set; } = null!;

        /// <summary>
        /// IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        /// </summary>
        [Output("roleArn")]
        public Output<string?> RoleArn { get; private set; } = null!;

        [Output("samlConfiguration")]
        public Output<Outputs.WorkspaceSamlConfiguration?> SamlConfiguration { get; private set; } = null!;

        [Output("samlConfigurationStatus")]
        public Output<Pulumi.AwsNative.Grafana.WorkspaceSamlConfigurationStatus> SamlConfigurationStatus { get; private set; } = null!;

        /// <summary>
        /// The client ID of the AWS SSO Managed Application.
        /// </summary>
        [Output("ssoClientId")]
        public Output<string> SsoClientId { get; private set; } = null!;

        /// <summary>
        /// The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        /// </summary>
        [Output("stackSetName")]
        public Output<string?> StackSetName { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.Grafana.WorkspaceStatus> Status { get; private set; } = null!;


        /// <summary>
        /// Create a Workspace resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Workspace(string name, WorkspaceArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:grafana:Workspace", name, args ?? new WorkspaceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Workspace(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:grafana:Workspace", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Workspace resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Workspace Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Workspace(name, id, options);
        }
    }

    public sealed class WorkspaceArgs : global::Pulumi.ResourceArgs
    {
        [Input("accountAccessType")]
        public Input<Pulumi.AwsNative.Grafana.WorkspaceAccountAccessType>? AccountAccessType { get; set; }

        [Input("authenticationProviders")]
        private InputList<Pulumi.AwsNative.Grafana.WorkspaceAuthenticationProviderTypes>? _authenticationProviders;

        /// <summary>
        /// List of authentication providers to enable.
        /// </summary>
        public InputList<Pulumi.AwsNative.Grafana.WorkspaceAuthenticationProviderTypes> AuthenticationProviders
        {
            get => _authenticationProviders ?? (_authenticationProviders = new InputList<Pulumi.AwsNative.Grafana.WorkspaceAuthenticationProviderTypes>());
            set => _authenticationProviders = value;
        }

        /// <summary>
        /// A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
        /// </summary>
        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        [Input("dataSources")]
        private InputList<Pulumi.AwsNative.Grafana.WorkspaceDataSourceType>? _dataSources;

        /// <summary>
        /// List of data sources on the service managed IAM role.
        /// </summary>
        public InputList<Pulumi.AwsNative.Grafana.WorkspaceDataSourceType> DataSources
        {
            get => _dataSources ?? (_dataSources = new InputList<Pulumi.AwsNative.Grafana.WorkspaceDataSourceType>());
            set => _dataSources = value;
        }

        /// <summary>
        /// Description of a workspace.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The user friendly name of a workspace.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("notificationDestinations")]
        private InputList<Pulumi.AwsNative.Grafana.WorkspaceNotificationDestinationType>? _notificationDestinations;

        /// <summary>
        /// List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        /// </summary>
        public InputList<Pulumi.AwsNative.Grafana.WorkspaceNotificationDestinationType> NotificationDestinations
        {
            get => _notificationDestinations ?? (_notificationDestinations = new InputList<Pulumi.AwsNative.Grafana.WorkspaceNotificationDestinationType>());
            set => _notificationDestinations = value;
        }

        /// <summary>
        /// The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        /// </summary>
        [Input("organizationRoleName")]
        public Input<string>? OrganizationRoleName { get; set; }

        [Input("organizationalUnits")]
        private InputList<string>? _organizationalUnits;

        /// <summary>
        /// List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        /// </summary>
        public InputList<string> OrganizationalUnits
        {
            get => _organizationalUnits ?? (_organizationalUnits = new InputList<string>());
            set => _organizationalUnits = value;
        }

        [Input("permissionType")]
        public Input<Pulumi.AwsNative.Grafana.WorkspacePermissionType>? PermissionType { get; set; }

        /// <summary>
        /// IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        /// </summary>
        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        [Input("samlConfiguration")]
        public Input<Inputs.WorkspaceSamlConfigurationArgs>? SamlConfiguration { get; set; }

        /// <summary>
        /// The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        /// </summary>
        [Input("stackSetName")]
        public Input<string>? StackSetName { get; set; }

        public WorkspaceArgs()
        {
        }
        public static new WorkspaceArgs Empty => new WorkspaceArgs();
    }
}
