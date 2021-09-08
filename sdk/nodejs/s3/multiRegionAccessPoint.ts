// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html
 */
export class MultiRegionAccessPoint extends pulumi.CustomResource {
    /**
     * Get an existing MultiRegionAccessPoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): MultiRegionAccessPoint {
        return new MultiRegionAccessPoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:s3:MultiRegionAccessPoint';

    /**
     * Returns true if the given object is an instance of MultiRegionAccessPoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MultiRegionAccessPoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MultiRegionAccessPoint.__pulumiType;
    }

    public /*out*/ readonly alias!: pulumi.Output<string>;
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-name
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration
     */
    public readonly publicAccessBlockConfiguration!: pulumi.Output<outputs.s3.MultiRegionAccessPointPublicAccessBlockConfiguration | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-regions
     */
    public readonly regions!: pulumi.Output<outputs.s3.MultiRegionAccessPointRegion[]>;

    /**
     * Create a MultiRegionAccessPoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MultiRegionAccessPointArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.regions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'regions'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["publicAccessBlockConfiguration"] = args ? args.publicAccessBlockConfiguration : undefined;
            inputs["regions"] = args ? args.regions : undefined;
            inputs["alias"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
        } else {
            inputs["alias"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["publicAccessBlockConfiguration"] = undefined /*out*/;
            inputs["regions"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(MultiRegionAccessPoint.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a MultiRegionAccessPoint resource.
 */
export interface MultiRegionAccessPointArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-name
     */
    name?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration
     */
    publicAccessBlockConfiguration?: pulumi.Input<inputs.s3.MultiRegionAccessPointPublicAccessBlockConfigurationArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-regions
     */
    regions: pulumi.Input<pulumi.Input<inputs.s3.MultiRegionAccessPointRegionArgs>[]>;
}
