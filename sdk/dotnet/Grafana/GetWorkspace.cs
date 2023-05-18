// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Grafana
{
    public static class GetWorkspace
    {
        /// <summary>
        /// Definition of AWS::Grafana::Workspace Resource Type
        /// </summary>
        public static Task<GetWorkspaceResult> InvokeAsync(GetWorkspaceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetWorkspaceResult>("aws-native:grafana:getWorkspace", args ?? new GetWorkspaceArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::Grafana::Workspace Resource Type
        /// </summary>
        public static Output<GetWorkspaceResult> Invoke(GetWorkspaceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetWorkspaceResult>("aws-native:grafana:getWorkspace", args ?? new GetWorkspaceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWorkspaceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The id that uniquely identifies a Grafana workspace.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetWorkspaceArgs()
        {
        }
        public static new GetWorkspaceArgs Empty => new GetWorkspaceArgs();
    }

    public sealed class GetWorkspaceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The id that uniquely identifies a Grafana workspace.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetWorkspaceInvokeArgs()
        {
        }
        public static new GetWorkspaceInvokeArgs Empty => new GetWorkspaceInvokeArgs();
    }


    [OutputType]
    public sealed class GetWorkspaceResult
    {
        public readonly Pulumi.AwsNative.Grafana.WorkspaceAccountAccessType? AccountAccessType;
        /// <summary>
        /// List of authentication providers to enable.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceAuthenticationProviderTypes> AuthenticationProviders;
        /// <summary>
        /// Timestamp when the workspace was created.
        /// </summary>
        public readonly string? CreationTimestamp;
        /// <summary>
        /// List of data sources on the service managed IAM role.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceDataSourceType> DataSources;
        /// <summary>
        /// Description of a workspace.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Endpoint for the Grafana workspace.
        /// </summary>
        public readonly string? Endpoint;
        /// <summary>
        /// Version of Grafana the workspace is currently using.
        /// </summary>
        public readonly string? GrafanaVersion;
        /// <summary>
        /// The id that uniquely identifies a Grafana workspace.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Timestamp when the workspace was last modified
        /// </summary>
        public readonly string? ModificationTimestamp;
        /// <summary>
        /// The user friendly name of a workspace.
        /// </summary>
        public readonly string? Name;
        public readonly Outputs.WorkspaceNetworkAccessControl? NetworkAccessControl;
        /// <summary>
        /// List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceNotificationDestinationType> NotificationDestinations;
        /// <summary>
        /// The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
        /// </summary>
        public readonly string? OrganizationRoleName;
        /// <summary>
        /// List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
        /// </summary>
        public readonly ImmutableArray<string> OrganizationalUnits;
        public readonly Pulumi.AwsNative.Grafana.WorkspacePermissionType? PermissionType;
        /// <summary>
        /// IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
        /// </summary>
        public readonly string? RoleArn;
        public readonly Outputs.WorkspaceSamlConfiguration? SamlConfiguration;
        public readonly Pulumi.AwsNative.Grafana.WorkspaceSamlConfigurationStatus? SamlConfigurationStatus;
        /// <summary>
        /// The client ID of the AWS SSO Managed Application.
        /// </summary>
        public readonly string? SsoClientId;
        /// <summary>
        /// The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
        /// </summary>
        public readonly string? StackSetName;
        public readonly Pulumi.AwsNative.Grafana.WorkspaceStatus? Status;
        public readonly Outputs.WorkspaceVpcConfiguration? VpcConfiguration;

        [OutputConstructor]
        private GetWorkspaceResult(
            Pulumi.AwsNative.Grafana.WorkspaceAccountAccessType? accountAccessType,

            ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceAuthenticationProviderTypes> authenticationProviders,

            string? creationTimestamp,

            ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceDataSourceType> dataSources,

            string? description,

            string? endpoint,

            string? grafanaVersion,

            string? id,

            string? modificationTimestamp,

            string? name,

            Outputs.WorkspaceNetworkAccessControl? networkAccessControl,

            ImmutableArray<Pulumi.AwsNative.Grafana.WorkspaceNotificationDestinationType> notificationDestinations,

            string? organizationRoleName,

            ImmutableArray<string> organizationalUnits,

            Pulumi.AwsNative.Grafana.WorkspacePermissionType? permissionType,

            string? roleArn,

            Outputs.WorkspaceSamlConfiguration? samlConfiguration,

            Pulumi.AwsNative.Grafana.WorkspaceSamlConfigurationStatus? samlConfigurationStatus,

            string? ssoClientId,

            string? stackSetName,

            Pulumi.AwsNative.Grafana.WorkspaceStatus? status,

            Outputs.WorkspaceVpcConfiguration? vpcConfiguration)
        {
            AccountAccessType = accountAccessType;
            AuthenticationProviders = authenticationProviders;
            CreationTimestamp = creationTimestamp;
            DataSources = dataSources;
            Description = description;
            Endpoint = endpoint;
            GrafanaVersion = grafanaVersion;
            Id = id;
            ModificationTimestamp = modificationTimestamp;
            Name = name;
            NetworkAccessControl = networkAccessControl;
            NotificationDestinations = notificationDestinations;
            OrganizationRoleName = organizationRoleName;
            OrganizationalUnits = organizationalUnits;
            PermissionType = permissionType;
            RoleArn = roleArn;
            SamlConfiguration = samlConfiguration;
            SamlConfigurationStatus = samlConfigurationStatus;
            SsoClientId = ssoClientId;
            StackSetName = stackSetName;
            Status = status;
            VpcConfiguration = vpcConfiguration;
        }
    }
}
