// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Definition of AWS::Grafana::Workspace Resource Type
 */
export function getWorkspace(args: GetWorkspaceArgs, opts?: pulumi.InvokeOptions): Promise<GetWorkspaceResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:grafana:getWorkspace", {
        "id": args.id,
    }, opts);
}

export interface GetWorkspaceArgs {
    /**
     * The id that uniquely identifies a Grafana workspace.
     */
    id: string;
}

export interface GetWorkspaceResult {
    readonly accountAccessType?: enums.grafana.WorkspaceAccountAccessType;
    /**
     * List of authentication providers to enable.
     */
    readonly authenticationProviders?: enums.grafana.WorkspaceAuthenticationProviderTypes[];
    /**
     * Timestamp when the workspace was created.
     */
    readonly creationTimestamp?: string;
    /**
     * List of data sources on the service managed IAM role.
     */
    readonly dataSources?: enums.grafana.WorkspaceDataSourceType[];
    /**
     * Description of a workspace.
     */
    readonly description?: string;
    /**
     * Endpoint for the Grafana workspace.
     */
    readonly endpoint?: string;
    /**
     * Version of Grafana the workspace is currently using.
     */
    readonly grafanaVersion?: string;
    /**
     * The id that uniquely identifies a Grafana workspace.
     */
    readonly id?: string;
    /**
     * Timestamp when the workspace was last modified
     */
    readonly modificationTimestamp?: string;
    /**
     * The user friendly name of a workspace.
     */
    readonly name?: string;
    /**
     * List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
     */
    readonly notificationDestinations?: enums.grafana.WorkspaceNotificationDestinationType[];
    /**
     * The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
     */
    readonly organizationRoleName?: string;
    /**
     * List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
     */
    readonly organizationalUnits?: string[];
    readonly permissionType?: enums.grafana.WorkspacePermissionType;
    /**
     * IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
     */
    readonly roleArn?: string;
    readonly samlConfiguration?: outputs.grafana.WorkspaceSamlConfiguration;
    readonly samlConfigurationStatus?: enums.grafana.WorkspaceSamlConfigurationStatus;
    /**
     * The client ID of the AWS SSO Managed Application.
     */
    readonly ssoClientId?: string;
    /**
     * The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
     */
    readonly stackSetName?: string;
    readonly status?: enums.grafana.WorkspaceStatus;
    readonly vpcConfiguration?: outputs.grafana.WorkspaceVpcConfiguration;
}

export function getWorkspaceOutput(args: GetWorkspaceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetWorkspaceResult> {
    return pulumi.output(args).apply(a => getWorkspace(a, opts))
}

export interface GetWorkspaceOutputArgs {
    /**
     * The id that uniquely identifies a Grafana workspace.
     */
    id: pulumi.Input<string>;
}
