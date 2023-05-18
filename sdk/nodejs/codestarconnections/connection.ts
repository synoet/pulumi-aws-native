// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Schema for AWS::CodeStarConnections::Connection resource which can be used to connect external source providers with AWS CodePipeline
 */
export class Connection extends pulumi.CustomResource {
    /**
     * Get an existing Connection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Connection {
        return new Connection(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codestarconnections:Connection';

    /**
     * Returns true if the given object is an instance of Connection.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Connection {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Connection.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the  connection. The ARN is used as the connection reference when the connection is shared between AWS services.
     */
    public /*out*/ readonly connectionArn!: pulumi.Output<string>;
    /**
     * The name of the connection. Connection names must be unique in an AWS user account.
     */
    public readonly connectionName!: pulumi.Output<string>;
    /**
     * The current status of the connection.
     */
    public /*out*/ readonly connectionStatus!: pulumi.Output<string>;
    /**
     * The host arn configured to represent the infrastructure where your third-party provider is installed. You must specify either a ProviderType or a HostArn.
     */
    public readonly hostArn!: pulumi.Output<string | undefined>;
    /**
     * The name of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.
     */
    public /*out*/ readonly ownerAccountId!: pulumi.Output<string>;
    /**
     * The name of the external provider where your third-party code repository is configured. You must specify either a ProviderType or a HostArn.
     */
    public readonly providerType!: pulumi.Output<string | undefined>;
    /**
     * Specifies the tags applied to a connection.
     */
    public readonly tags!: pulumi.Output<outputs.codestarconnections.ConnectionTag[] | undefined>;

    /**
     * Create a Connection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ConnectionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["connectionName"] = args ? args.connectionName : undefined;
            resourceInputs["hostArn"] = args ? args.hostArn : undefined;
            resourceInputs["providerType"] = args ? args.providerType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["connectionArn"] = undefined /*out*/;
            resourceInputs["connectionStatus"] = undefined /*out*/;
            resourceInputs["ownerAccountId"] = undefined /*out*/;
        } else {
            resourceInputs["connectionArn"] = undefined /*out*/;
            resourceInputs["connectionName"] = undefined /*out*/;
            resourceInputs["connectionStatus"] = undefined /*out*/;
            resourceInputs["hostArn"] = undefined /*out*/;
            resourceInputs["ownerAccountId"] = undefined /*out*/;
            resourceInputs["providerType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Connection.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Connection resource.
 */
export interface ConnectionArgs {
    /**
     * The name of the connection. Connection names must be unique in an AWS user account.
     */
    connectionName?: pulumi.Input<string>;
    /**
     * The host arn configured to represent the infrastructure where your third-party provider is installed. You must specify either a ProviderType or a HostArn.
     */
    hostArn?: pulumi.Input<string>;
    /**
     * The name of the external provider where your third-party code repository is configured. You must specify either a ProviderType or a HostArn.
     */
    providerType?: pulumi.Input<string>;
    /**
     * Specifies the tags applied to a connection.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.codestarconnections.ConnectionTagArgs>[]>;
}
