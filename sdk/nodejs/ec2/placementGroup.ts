// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::PlacementGroup
 *
 * @deprecated PlacementGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class PlacementGroup extends pulumi.CustomResource {
    /**
     * Get an existing PlacementGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): PlacementGroup {
        pulumi.log.warn("PlacementGroup is deprecated: PlacementGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new PlacementGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:PlacementGroup';

    /**
     * Returns true if the given object is an instance of PlacementGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PlacementGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PlacementGroup.__pulumiType;
    }

    public readonly strategy!: pulumi.Output<string | undefined>;

    /**
     * Create a PlacementGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated PlacementGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: PlacementGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("PlacementGroup is deprecated: PlacementGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["strategy"] = args ? args.strategy : undefined;
        } else {
            inputs["strategy"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(PlacementGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a PlacementGroup resource.
 */
export interface PlacementGroupArgs {
    strategy?: pulumi.Input<string>;
}
