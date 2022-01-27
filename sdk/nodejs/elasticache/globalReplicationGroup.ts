// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::ElastiCache::GlobalReplicationGroup resource creates an Amazon ElastiCache Global Replication Group.
 */
export class GlobalReplicationGroup extends pulumi.CustomResource {
    /**
     * Get an existing GlobalReplicationGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): GlobalReplicationGroup {
        return new GlobalReplicationGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticache:GlobalReplicationGroup';

    /**
     * Returns true if the given object is an instance of GlobalReplicationGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GlobalReplicationGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GlobalReplicationGroup.__pulumiType;
    }

    /**
     * AutomaticFailoverEnabled
     */
    public readonly automaticFailoverEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The cache node type of the Global Datastore
     */
    public readonly cacheNodeType!: pulumi.Output<string | undefined>;
    /**
     * Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.
     */
    public readonly cacheParameterGroupName!: pulumi.Output<string | undefined>;
    /**
     * The engine version of the Global Datastore.
     */
    public readonly engineVersion!: pulumi.Output<string | undefined>;
    /**
     * Indicates the number of node groups in the Global Datastore.
     */
    public readonly globalNodeGroupCount!: pulumi.Output<number | undefined>;
    /**
     * The optional description of the Global Datastore
     */
    public readonly globalReplicationGroupDescription!: pulumi.Output<string | undefined>;
    /**
     * The name of the Global Datastore, it is generated by ElastiCache adding a prefix to GlobalReplicationGroupIdSuffix.
     */
    public /*out*/ readonly globalReplicationGroupId!: pulumi.Output<string>;
    /**
     * The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. 
     */
    public readonly globalReplicationGroupIdSuffix!: pulumi.Output<string | undefined>;
    /**
     * The replication groups that comprise the Global Datastore.
     */
    public readonly members!: pulumi.Output<outputs.elasticache.GlobalReplicationGroupMember[]>;
    /**
     * Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore 
     */
    public readonly regionalConfigurations!: pulumi.Output<outputs.elasticache.GlobalReplicationGroupRegionalConfiguration[] | undefined>;
    /**
     * The status of the Global Datastore
     */
    public /*out*/ readonly status!: pulumi.Output<string>;

    /**
     * Create a GlobalReplicationGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GlobalReplicationGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.members === undefined) && !opts.urn) {
                throw new Error("Missing required property 'members'");
            }
            resourceInputs["automaticFailoverEnabled"] = args ? args.automaticFailoverEnabled : undefined;
            resourceInputs["cacheNodeType"] = args ? args.cacheNodeType : undefined;
            resourceInputs["cacheParameterGroupName"] = args ? args.cacheParameterGroupName : undefined;
            resourceInputs["engineVersion"] = args ? args.engineVersion : undefined;
            resourceInputs["globalNodeGroupCount"] = args ? args.globalNodeGroupCount : undefined;
            resourceInputs["globalReplicationGroupDescription"] = args ? args.globalReplicationGroupDescription : undefined;
            resourceInputs["globalReplicationGroupIdSuffix"] = args ? args.globalReplicationGroupIdSuffix : undefined;
            resourceInputs["members"] = args ? args.members : undefined;
            resourceInputs["regionalConfigurations"] = args ? args.regionalConfigurations : undefined;
            resourceInputs["globalReplicationGroupId"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["automaticFailoverEnabled"] = undefined /*out*/;
            resourceInputs["cacheNodeType"] = undefined /*out*/;
            resourceInputs["cacheParameterGroupName"] = undefined /*out*/;
            resourceInputs["engineVersion"] = undefined /*out*/;
            resourceInputs["globalNodeGroupCount"] = undefined /*out*/;
            resourceInputs["globalReplicationGroupDescription"] = undefined /*out*/;
            resourceInputs["globalReplicationGroupId"] = undefined /*out*/;
            resourceInputs["globalReplicationGroupIdSuffix"] = undefined /*out*/;
            resourceInputs["members"] = undefined /*out*/;
            resourceInputs["regionalConfigurations"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GlobalReplicationGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a GlobalReplicationGroup resource.
 */
export interface GlobalReplicationGroupArgs {
    /**
     * AutomaticFailoverEnabled
     */
    automaticFailoverEnabled?: pulumi.Input<boolean>;
    /**
     * The cache node type of the Global Datastore
     */
    cacheNodeType?: pulumi.Input<string>;
    /**
     * Cache parameter group name to use for the new engine version. This parameter cannot be modified independently.
     */
    cacheParameterGroupName?: pulumi.Input<string>;
    /**
     * The engine version of the Global Datastore.
     */
    engineVersion?: pulumi.Input<string>;
    /**
     * Indicates the number of node groups in the Global Datastore.
     */
    globalNodeGroupCount?: pulumi.Input<number>;
    /**
     * The optional description of the Global Datastore
     */
    globalReplicationGroupDescription?: pulumi.Input<string>;
    /**
     * The suffix name of a Global Datastore. Amazon ElastiCache automatically applies a prefix to the Global Datastore ID when it is created. Each AWS Region has its own prefix. 
     */
    globalReplicationGroupIdSuffix?: pulumi.Input<string>;
    /**
     * The replication groups that comprise the Global Datastore.
     */
    members: pulumi.Input<pulumi.Input<inputs.elasticache.GlobalReplicationGroupMemberArgs>[]>;
    /**
     * Describes the replication group IDs, the AWS regions where they are stored and the shard configuration for each that comprise the Global Datastore 
     */
    regionalConfigurations?: pulumi.Input<pulumi.Input<inputs.elasticache.GlobalReplicationGroupRegionalConfigurationArgs>[]>;
}
