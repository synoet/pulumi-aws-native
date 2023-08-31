// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Route53Resolver::OutpostResolver.
 */
export class OutpostResolver extends pulumi.CustomResource {
    /**
     * Get an existing OutpostResolver resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): OutpostResolver {
        return new OutpostResolver(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53resolver:OutpostResolver';

    /**
     * Returns true if the given object is an instance of OutpostResolver.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OutpostResolver {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OutpostResolver.__pulumiType;
    }

    /**
     * The OutpostResolver ARN.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The OutpostResolver creation time
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * The id of the creator request.
     */
    public /*out*/ readonly creatorRequestId!: pulumi.Output<string>;
    /**
     * The number of OutpostResolvers.
     */
    public readonly instanceCount!: pulumi.Output<number | undefined>;
    /**
     * The OutpostResolver last modified time
     */
    public /*out*/ readonly modificationTime!: pulumi.Output<string>;
    /**
     * The OutpostResolver name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Outpost ARN.
     */
    public readonly outpostArn!: pulumi.Output<string>;
    /**
     * The OutpostResolver instance type.
     */
    public readonly preferredInstanceType!: pulumi.Output<string>;
    /**
     * The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.
     */
    public /*out*/ readonly status!: pulumi.Output<enums.route53resolver.OutpostResolverStatus>;
    /**
     * The OutpostResolver status message.
     */
    public /*out*/ readonly statusMessage!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.route53resolver.OutpostResolverTag[] | undefined>;

    /**
     * Create a OutpostResolver resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OutpostResolverArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.outpostArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'outpostArn'");
            }
            if ((!args || args.preferredInstanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'preferredInstanceType'");
            }
            resourceInputs["instanceCount"] = args ? args.instanceCount : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["outpostArn"] = args ? args.outpostArn : undefined;
            resourceInputs["preferredInstanceType"] = args ? args.preferredInstanceType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["creatorRequestId"] = undefined /*out*/;
            resourceInputs["modificationTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["statusMessage"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["creatorRequestId"] = undefined /*out*/;
            resourceInputs["instanceCount"] = undefined /*out*/;
            resourceInputs["modificationTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["outpostArn"] = undefined /*out*/;
            resourceInputs["preferredInstanceType"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["statusMessage"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["outpostArn"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(OutpostResolver.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a OutpostResolver resource.
 */
export interface OutpostResolverArgs {
    /**
     * The number of OutpostResolvers.
     */
    instanceCount?: pulumi.Input<number>;
    /**
     * The OutpostResolver name.
     */
    name?: pulumi.Input<string>;
    /**
     * The Outpost ARN.
     */
    outpostArn: pulumi.Input<string>;
    /**
     * The OutpostResolver instance type.
     */
    preferredInstanceType: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.route53resolver.OutpostResolverTagArgs>[]>;
}
