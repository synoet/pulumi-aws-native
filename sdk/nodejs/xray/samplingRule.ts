// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * This schema provides construct and validation rules for AWS-XRay SamplingRule resource parameters.
 */
export class SamplingRule extends pulumi.CustomResource {
    /**
     * Get an existing SamplingRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SamplingRule {
        return new SamplingRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:xray:SamplingRule';

    /**
     * Returns true if the given object is an instance of SamplingRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SamplingRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SamplingRule.__pulumiType;
    }

    public /*out*/ readonly ruleArn!: pulumi.Output<string>;
    public readonly ruleName!: pulumi.Output<string | undefined>;
    public readonly samplingRule!: pulumi.Output<outputs.xray.SamplingRule | undefined>;
    public readonly samplingRuleRecord!: pulumi.Output<outputs.xray.SamplingRuleRecord | undefined>;
    public readonly samplingRuleUpdate!: pulumi.Output<outputs.xray.SamplingRuleUpdate | undefined>;
    public readonly tags!: pulumi.Output<outputs.xray.SamplingRuleTag[] | undefined>;

    /**
     * Create a SamplingRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SamplingRuleArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["ruleName"] = args ? args.ruleName : undefined;
            resourceInputs["samplingRule"] = args ? args.samplingRule : undefined;
            resourceInputs["samplingRuleRecord"] = args ? args.samplingRuleRecord : undefined;
            resourceInputs["samplingRuleUpdate"] = args ? args.samplingRuleUpdate : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["ruleArn"] = undefined /*out*/;
        } else {
            resourceInputs["ruleArn"] = undefined /*out*/;
            resourceInputs["ruleName"] = undefined /*out*/;
            resourceInputs["samplingRule"] = undefined /*out*/;
            resourceInputs["samplingRuleRecord"] = undefined /*out*/;
            resourceInputs["samplingRuleUpdate"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SamplingRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SamplingRule resource.
 */
export interface SamplingRuleArgs {
    ruleName?: pulumi.Input<string>;
    samplingRule?: pulumi.Input<inputs.xray.SamplingRuleArgs>;
    samplingRuleRecord?: pulumi.Input<inputs.xray.SamplingRuleRecordArgs>;
    samplingRuleUpdate?: pulumi.Input<inputs.xray.SamplingRuleUpdateArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.xray.SamplingRuleTagArgs>[]>;
}
