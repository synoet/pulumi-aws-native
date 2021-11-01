// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Route53Resolver::ResolverConfig.
 */
export class ResolverConfig extends pulumi.CustomResource {
    /**
     * Get an existing ResolverConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ResolverConfig {
        return new ResolverConfig(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53resolver:ResolverConfig';

    /**
     * Returns true if the given object is an instance of ResolverConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ResolverConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ResolverConfig.__pulumiType;
    }

    /**
     * ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
     */
    public /*out*/ readonly autodefinedReverse!: pulumi.Output<enums.route53resolver.ResolverConfigAutodefinedReverse>;
    /**
     * Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
     */
    public readonly autodefinedReverseFlag!: pulumi.Output<enums.route53resolver.ResolverConfigAutodefinedReverseFlag>;
    /**
     * AccountId
     */
    public /*out*/ readonly ownerId!: pulumi.Output<string>;
    /**
     * ResourceId
     */
    public readonly resourceId!: pulumi.Output<string>;

    /**
     * Create a ResolverConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ResolverConfigArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.autodefinedReverseFlag === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autodefinedReverseFlag'");
            }
            if ((!args || args.resourceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceId'");
            }
            inputs["autodefinedReverseFlag"] = args ? args.autodefinedReverseFlag : undefined;
            inputs["resourceId"] = args ? args.resourceId : undefined;
            inputs["autodefinedReverse"] = undefined /*out*/;
            inputs["ownerId"] = undefined /*out*/;
        } else {
            inputs["autodefinedReverse"] = undefined /*out*/;
            inputs["autodefinedReverseFlag"] = undefined /*out*/;
            inputs["ownerId"] = undefined /*out*/;
            inputs["resourceId"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ResolverConfig.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ResolverConfig resource.
 */
export interface ResolverConfigArgs {
    /**
     * Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
     */
    autodefinedReverseFlag: pulumi.Input<enums.route53resolver.ResolverConfigAutodefinedReverseFlag>;
    /**
     * ResourceId
     */
    resourceId: pulumi.Input<string>;
}
