// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.
 */
export class CostCategory extends pulumi.CustomResource {
    /**
     * Get an existing CostCategory resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CostCategory {
        return new CostCategory(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ce:CostCategory';

    /**
     * Returns true if the given object is an instance of CostCategory.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CostCategory {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CostCategory.__pulumiType;
    }

    /**
     * Cost category ARN
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The default value for the cost category
     */
    public readonly defaultValue!: pulumi.Output<string | undefined>;
    public /*out*/ readonly effectiveStart!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly ruleVersion!: pulumi.Output<enums.ce.CostCategoryRuleVersion>;
    /**
     * JSON array format of Expression in Billing and Cost Management API
     */
    public readonly rules!: pulumi.Output<string>;
    /**
     * Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
     */
    public readonly splitChargeRules!: pulumi.Output<string | undefined>;

    /**
     * Create a CostCategory resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CostCategoryArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.ruleVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ruleVersion'");
            }
            if ((!args || args.rules === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rules'");
            }
            resourceInputs["defaultValue"] = args ? args.defaultValue : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["ruleVersion"] = args ? args.ruleVersion : undefined;
            resourceInputs["rules"] = args ? args.rules : undefined;
            resourceInputs["splitChargeRules"] = args ? args.splitChargeRules : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["effectiveStart"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["defaultValue"] = undefined /*out*/;
            resourceInputs["effectiveStart"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["ruleVersion"] = undefined /*out*/;
            resourceInputs["rules"] = undefined /*out*/;
            resourceInputs["splitChargeRules"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(CostCategory.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a CostCategory resource.
 */
export interface CostCategoryArgs {
    /**
     * The default value for the cost category
     */
    defaultValue?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    ruleVersion: pulumi.Input<enums.ce.CostCategoryRuleVersion>;
    /**
     * JSON array format of Expression in Billing and Cost Management API
     */
    rules: pulumi.Input<string>;
    /**
     * Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
     */
    splitChargeRules?: pulumi.Input<string>;
}
