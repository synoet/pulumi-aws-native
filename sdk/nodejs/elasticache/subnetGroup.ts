// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElastiCache::SubnetGroup
 */
export class SubnetGroup extends pulumi.CustomResource {
    /**
     * Get an existing SubnetGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SubnetGroup {
        return new SubnetGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticache:SubnetGroup';

    /**
     * Returns true if the given object is an instance of SubnetGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SubnetGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SubnetGroup.__pulumiType;
    }

    /**
     * The name for the cache subnet group. This value is stored as a lowercase string.
     */
    public readonly cacheSubnetGroupName!: pulumi.Output<string | undefined>;
    /**
     * The description for the cache subnet group.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The EC2 subnet IDs for the cache subnet group.
     */
    public readonly subnetIds!: pulumi.Output<string[]>;
    public readonly tags!: pulumi.Output<outputs.elasticache.SubnetGroupTag[] | undefined>;

    /**
     * Create a SubnetGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SubnetGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.subnetIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetIds'");
            }
            resourceInputs["cacheSubnetGroupName"] = args ? args.cacheSubnetGroupName : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["subnetIds"] = args ? args.subnetIds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["cacheSubnetGroupName"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["subnetIds"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["cacheSubnetGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(SubnetGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SubnetGroup resource.
 */
export interface SubnetGroupArgs {
    /**
     * The name for the cache subnet group. This value is stored as a lowercase string.
     */
    cacheSubnetGroupName?: pulumi.Input<string>;
    /**
     * The description for the cache subnet group.
     */
    description: pulumi.Input<string>;
    /**
     * The EC2 subnet IDs for the cache subnet group.
     */
    subnetIds: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.elasticache.SubnetGroupTagArgs>[]>;
}
