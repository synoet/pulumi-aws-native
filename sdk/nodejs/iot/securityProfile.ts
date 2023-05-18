// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A security profile defines a set of expected behaviors for devices in your account.
 */
export class SecurityProfile extends pulumi.CustomResource {
    /**
     * Get an existing SecurityProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SecurityProfile {
        return new SecurityProfile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iot:SecurityProfile';

    /**
     * Returns true if the given object is an instance of SecurityProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SecurityProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SecurityProfile.__pulumiType;
    }

    /**
     * A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.
     */
    public readonly additionalMetricsToRetainV2!: pulumi.Output<outputs.iot.SecurityProfileMetricToRetain[] | undefined>;
    /**
     * Specifies the destinations to which alerts are sent.
     */
    public readonly alertTargets!: pulumi.Output<any | undefined>;
    /**
     * Specifies the behaviors that, when violated by a device (thing), cause an alert.
     */
    public readonly behaviors!: pulumi.Output<outputs.iot.SecurityProfileBehavior[] | undefined>;
    /**
     * The ARN (Amazon resource name) of the created security profile.
     */
    public /*out*/ readonly securityProfileArn!: pulumi.Output<string>;
    /**
     * A description of the security profile.
     */
    public readonly securityProfileDescription!: pulumi.Output<string | undefined>;
    /**
     * A unique identifier for the security profile.
     */
    public readonly securityProfileName!: pulumi.Output<string | undefined>;
    /**
     * Metadata that can be used to manage the security profile.
     */
    public readonly tags!: pulumi.Output<outputs.iot.SecurityProfileTag[] | undefined>;
    /**
     * A set of target ARNs that the security profile is attached to.
     */
    public readonly targetArns!: pulumi.Output<string[] | undefined>;

    /**
     * Create a SecurityProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SecurityProfileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["additionalMetricsToRetainV2"] = args ? args.additionalMetricsToRetainV2 : undefined;
            resourceInputs["alertTargets"] = args ? args.alertTargets : undefined;
            resourceInputs["behaviors"] = args ? args.behaviors : undefined;
            resourceInputs["securityProfileDescription"] = args ? args.securityProfileDescription : undefined;
            resourceInputs["securityProfileName"] = args ? args.securityProfileName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["targetArns"] = args ? args.targetArns : undefined;
            resourceInputs["securityProfileArn"] = undefined /*out*/;
        } else {
            resourceInputs["additionalMetricsToRetainV2"] = undefined /*out*/;
            resourceInputs["alertTargets"] = undefined /*out*/;
            resourceInputs["behaviors"] = undefined /*out*/;
            resourceInputs["securityProfileArn"] = undefined /*out*/;
            resourceInputs["securityProfileDescription"] = undefined /*out*/;
            resourceInputs["securityProfileName"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["targetArns"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SecurityProfile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SecurityProfile resource.
 */
export interface SecurityProfileArgs {
    /**
     * A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.
     */
    additionalMetricsToRetainV2?: pulumi.Input<pulumi.Input<inputs.iot.SecurityProfileMetricToRetainArgs>[]>;
    /**
     * Specifies the destinations to which alerts are sent.
     */
    alertTargets?: any;
    /**
     * Specifies the behaviors that, when violated by a device (thing), cause an alert.
     */
    behaviors?: pulumi.Input<pulumi.Input<inputs.iot.SecurityProfileBehaviorArgs>[]>;
    /**
     * A description of the security profile.
     */
    securityProfileDescription?: pulumi.Input<string>;
    /**
     * A unique identifier for the security profile.
     */
    securityProfileName?: pulumi.Input<string>;
    /**
     * Metadata that can be used to manage the security profile.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.iot.SecurityProfileTagArgs>[]>;
    /**
     * A set of target ARNs that the security profile is attached to.
     */
    targetArns?: pulumi.Input<pulumi.Input<string>[]>;
}
