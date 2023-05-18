// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudWatch::InsightRule
 *
 * @deprecated InsightRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class InsightRule extends pulumi.CustomResource {
    /**
     * Get an existing InsightRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): InsightRule {
        pulumi.log.warn("InsightRule is deprecated: InsightRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new InsightRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudwatch:InsightRule';

    /**
     * Returns true if the given object is an instance of InsightRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is InsightRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === InsightRule.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly ruleBody!: pulumi.Output<string>;
    public readonly ruleName!: pulumi.Output<string>;
    public readonly ruleState!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.cloudwatch.InsightRuleTags | undefined>;

    /**
     * Create a InsightRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated InsightRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: InsightRuleArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("InsightRule is deprecated: InsightRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.ruleBody === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ruleBody'");
            }
            if ((!args || args.ruleName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ruleName'");
            }
            if ((!args || args.ruleState === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ruleState'");
            }
            resourceInputs["ruleBody"] = args ? args.ruleBody : undefined;
            resourceInputs["ruleName"] = args ? args.ruleName : undefined;
            resourceInputs["ruleState"] = args ? args.ruleState : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["ruleBody"] = undefined /*out*/;
            resourceInputs["ruleName"] = undefined /*out*/;
            resourceInputs["ruleState"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(InsightRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a InsightRule resource.
 */
export interface InsightRuleArgs {
    ruleBody: pulumi.Input<string>;
    ruleName: pulumi.Input<string>;
    ruleState: pulumi.Input<string>;
    tags?: pulumi.Input<inputs.cloudwatch.InsightRuleTagsArgs>;
}
