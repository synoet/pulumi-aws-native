// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::WAFRegional::Rule
 *
 * @deprecated Rule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Rule extends pulumi.CustomResource {
    /**
     * Get an existing Rule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Rule {
        pulumi.log.warn("Rule is deprecated: Rule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Rule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:wafregional:Rule';

    /**
     * Returns true if the given object is an instance of Rule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rule.__pulumiType;
    }

    public readonly metricName!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly predicates!: pulumi.Output<outputs.wafregional.RulePredicate[] | undefined>;

    /**
     * Create a Rule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Rule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: RuleArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Rule is deprecated: Rule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.metricName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'metricName'");
            }
            inputs["metricName"] = args ? args.metricName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["predicates"] = args ? args.predicates : undefined;
        } else {
            inputs["metricName"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["predicates"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Rule.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Rule resource.
 */
export interface RuleArgs {
    metricName: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    predicates?: pulumi.Input<pulumi.Input<inputs.wafregional.RulePredicateArgs>[]>;
}
