// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::GuardDuty::Detector
 *
 * @deprecated Detector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Detector extends pulumi.CustomResource {
    /**
     * Get an existing Detector resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Detector {
        pulumi.log.warn("Detector is deprecated: Detector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Detector(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:guardduty:Detector';

    /**
     * Returns true if the given object is an instance of Detector.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Detector {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Detector.__pulumiType;
    }

    public readonly dataSources!: pulumi.Output<outputs.guardduty.DetectorCFNDataSourceConfigurations | undefined>;
    public readonly enable!: pulumi.Output<boolean>;
    public readonly features!: pulumi.Output<outputs.guardduty.DetectorFeatureConfigurations[] | undefined>;
    public readonly findingPublishingFrequency!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.guardduty.DetectorTag[] | undefined>;

    /**
     * Create a Detector resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Detector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DetectorArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Detector is deprecated: Detector is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.enable === undefined) && !opts.urn) {
                throw new Error("Missing required property 'enable'");
            }
            resourceInputs["dataSources"] = args ? args.dataSources : undefined;
            resourceInputs["enable"] = args ? args.enable : undefined;
            resourceInputs["features"] = args ? args.features : undefined;
            resourceInputs["findingPublishingFrequency"] = args ? args.findingPublishingFrequency : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["dataSources"] = undefined /*out*/;
            resourceInputs["enable"] = undefined /*out*/;
            resourceInputs["features"] = undefined /*out*/;
            resourceInputs["findingPublishingFrequency"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Detector.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Detector resource.
 */
export interface DetectorArgs {
    dataSources?: pulumi.Input<inputs.guardduty.DetectorCFNDataSourceConfigurationsArgs>;
    enable: pulumi.Input<boolean>;
    features?: pulumi.Input<pulumi.Input<inputs.guardduty.DetectorFeatureConfigurationsArgs>[]>;
    findingPublishingFrequency?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.guardduty.DetectorTagArgs>[]>;
}
