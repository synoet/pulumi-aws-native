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
export class Workspace extends pulumi.CustomResource {
    /**
     * Get an existing Workspace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Workspace {
        return new Workspace(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:grafana:Workspace';

    /**
     * Returns true if the given object is an instance of Workspace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Workspace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Workspace.__pulumiType;
    }

    public readonly accountAccessType!: pulumi.Output<enums.grafana.WorkspaceAccountAccessType | undefined>;
    /**
     * List of authentication providers to enable.
     */
    public readonly authenticationProviders!: pulumi.Output<enums.grafana.WorkspaceAuthenticationProviderTypes[] | undefined>;
    /**
     * A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
     */
    public readonly clientToken!: pulumi.Output<string | undefined>;
    /**
     * Timestamp when the workspace was created.
     */
    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    /**
     * List of data sources on the service managed IAM role.
     */
    public readonly dataSources!: pulumi.Output<enums.grafana.WorkspaceDataSourceType[] | undefined>;
    /**
     * Description of a workspace.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Endpoint for the Grafana workspace.
     */
    public /*out*/ readonly endpoint!: pulumi.Output<string>;
    /**
     * Version of Grafana the workspace is currently using.
     */
    public /*out*/ readonly grafanaVersion!: pulumi.Output<string>;
    /**
     * Timestamp when the workspace was last modified
     */
    public /*out*/ readonly modificationTimestamp!: pulumi.Output<string>;
    /**
     * The user friendly name of a workspace.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
     */
    public readonly notificationDestinations!: pulumi.Output<enums.grafana.WorkspaceNotificationDestinationType[] | undefined>;
    /**
     * The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
     */
    public readonly organizationRoleName!: pulumi.Output<string | undefined>;
    /**
     * List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
     */
    public readonly organizationalUnits!: pulumi.Output<string[] | undefined>;
    public readonly permissionType!: pulumi.Output<enums.grafana.WorkspacePermissionType | undefined>;
    /**
     * IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
     */
    public readonly roleArn!: pulumi.Output<string | undefined>;
    public readonly samlConfiguration!: pulumi.Output<outputs.grafana.WorkspaceSamlConfiguration | undefined>;
    public /*out*/ readonly samlConfigurationStatus!: pulumi.Output<enums.grafana.WorkspaceSamlConfigurationStatus>;
    /**
     * The client ID of the AWS SSO Managed Application.
     */
    public /*out*/ readonly ssoClientId!: pulumi.Output<string>;
    /**
     * The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
     */
    public readonly stackSetName!: pulumi.Output<string | undefined>;
    public /*out*/ readonly status!: pulumi.Output<enums.grafana.WorkspaceStatus>;

    /**
     * Create a Workspace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: WorkspaceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["accountAccessType"] = args ? args.accountAccessType : undefined;
            resourceInputs["authenticationProviders"] = args ? args.authenticationProviders : undefined;
            resourceInputs["clientToken"] = args ? args.clientToken : undefined;
            resourceInputs["dataSources"] = args ? args.dataSources : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["notificationDestinations"] = args ? args.notificationDestinations : undefined;
            resourceInputs["organizationRoleName"] = args ? args.organizationRoleName : undefined;
            resourceInputs["organizationalUnits"] = args ? args.organizationalUnits : undefined;
            resourceInputs["permissionType"] = args ? args.permissionType : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["samlConfiguration"] = args ? args.samlConfiguration : undefined;
            resourceInputs["stackSetName"] = args ? args.stackSetName : undefined;
            resourceInputs["creationTimestamp"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["grafanaVersion"] = undefined /*out*/;
            resourceInputs["modificationTimestamp"] = undefined /*out*/;
            resourceInputs["samlConfigurationStatus"] = undefined /*out*/;
            resourceInputs["ssoClientId"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["accountAccessType"] = undefined /*out*/;
            resourceInputs["authenticationProviders"] = undefined /*out*/;
            resourceInputs["clientToken"] = undefined /*out*/;
            resourceInputs["creationTimestamp"] = undefined /*out*/;
            resourceInputs["dataSources"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["grafanaVersion"] = undefined /*out*/;
            resourceInputs["modificationTimestamp"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["notificationDestinations"] = undefined /*out*/;
            resourceInputs["organizationRoleName"] = undefined /*out*/;
            resourceInputs["organizationalUnits"] = undefined /*out*/;
            resourceInputs["permissionType"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["samlConfiguration"] = undefined /*out*/;
            resourceInputs["samlConfigurationStatus"] = undefined /*out*/;
            resourceInputs["ssoClientId"] = undefined /*out*/;
            resourceInputs["stackSetName"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Workspace.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Workspace resource.
 */
export interface WorkspaceArgs {
    accountAccessType?: pulumi.Input<enums.grafana.WorkspaceAccountAccessType>;
    /**
     * List of authentication providers to enable.
     */
    authenticationProviders?: pulumi.Input<pulumi.Input<enums.grafana.WorkspaceAuthenticationProviderTypes>[]>;
    /**
     * A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.
     */
    clientToken?: pulumi.Input<string>;
    /**
     * List of data sources on the service managed IAM role.
     */
    dataSources?: pulumi.Input<pulumi.Input<enums.grafana.WorkspaceDataSourceType>[]>;
    /**
     * Description of a workspace.
     */
    description?: pulumi.Input<string>;
    /**
     * The user friendly name of a workspace.
     */
    name?: pulumi.Input<string>;
    /**
     * List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.
     */
    notificationDestinations?: pulumi.Input<pulumi.Input<enums.grafana.WorkspaceNotificationDestinationType>[]>;
    /**
     * The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.
     */
    organizationRoleName?: pulumi.Input<string>;
    /**
     * List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.
     */
    organizationalUnits?: pulumi.Input<pulumi.Input<string>[]>;
    permissionType?: pulumi.Input<enums.grafana.WorkspacePermissionType>;
    /**
     * IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.
     */
    roleArn?: pulumi.Input<string>;
    samlConfiguration?: pulumi.Input<inputs.grafana.WorkspaceSamlConfigurationArgs>;
    /**
     * The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.
     */
    stackSetName?: pulumi.Input<string>;
}
