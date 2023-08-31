// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.
 */
export class SafetyRule extends pulumi.CustomResource {
    /**
     * Get an existing SafetyRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SafetyRule {
        return new SafetyRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53recoverycontrol:SafetyRule';

    /**
     * Returns true if the given object is an instance of SafetyRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SafetyRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SafetyRule.__pulumiType;
    }

    public readonly assertionRule!: pulumi.Output<outputs.route53recoverycontrol.SafetyRuleAssertionRule | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the control panel.
     */
    public readonly controlPanelArn!: pulumi.Output<string | undefined>;
    public readonly gatingRule!: pulumi.Output<outputs.route53recoverycontrol.SafetyRuleGatingRule | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly ruleConfig!: pulumi.Output<outputs.route53recoverycontrol.SafetyRuleRuleConfig | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the safety rule.
     */
    public /*out*/ readonly safetyRuleArn!: pulumi.Output<string>;
    /**
     * The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.
     */
    public /*out*/ readonly status!: pulumi.Output<enums.route53recoverycontrol.SafetyRuleStatus>;
    /**
     * A collection of tags associated with a resource
     */
    public readonly tags!: pulumi.Output<outputs.route53recoverycontrol.SafetyRuleTag[] | undefined>;

    /**
     * Create a SafetyRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: SafetyRuleArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["assertionRule"] = args ? args.assertionRule : undefined;
            resourceInputs["controlPanelArn"] = args ? args.controlPanelArn : undefined;
            resourceInputs["gatingRule"] = args ? args.gatingRule : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["ruleConfig"] = args ? args.ruleConfig : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["safetyRuleArn"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["assertionRule"] = undefined /*out*/;
            resourceInputs["controlPanelArn"] = undefined /*out*/;
            resourceInputs["gatingRule"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["ruleConfig"] = undefined /*out*/;
            resourceInputs["safetyRuleArn"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["controlPanelArn", "ruleConfig", "tags[*]"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(SafetyRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SafetyRule resource.
 */
export interface SafetyRuleArgs {
    assertionRule?: pulumi.Input<inputs.route53recoverycontrol.SafetyRuleAssertionRuleArgs>;
    /**
     * The Amazon Resource Name (ARN) of the control panel.
     */
    controlPanelArn?: pulumi.Input<string>;
    gatingRule?: pulumi.Input<inputs.route53recoverycontrol.SafetyRuleGatingRuleArgs>;
    name?: pulumi.Input<string>;
    ruleConfig?: pulumi.Input<inputs.route53recoverycontrol.SafetyRuleRuleConfigArgs>;
    /**
     * A collection of tags associated with a resource
     */
    tags?: pulumi.Input<pulumi.Input<inputs.route53recoverycontrol.SafetyRuleTagArgs>[]>;
}
