// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account
 */
export class Analyzer extends pulumi.CustomResource {
    /**
     * Get an existing Analyzer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Analyzer {
        return new Analyzer(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:accessanalyzer:Analyzer';

    /**
     * Returns true if the given object is an instance of Analyzer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Analyzer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Analyzer.__pulumiType;
    }

    /**
     * Analyzer name
     */
    public readonly analyzerName!: pulumi.Output<string | undefined>;
    public readonly archiveRules!: pulumi.Output<outputs.accessanalyzer.AnalyzerArchiveRule[] | undefined>;
    /**
     * Amazon Resource Name (ARN) of the analyzer
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.accessanalyzer.AnalyzerTag[] | undefined>;
    /**
     * The type of the analyzer, must be ACCOUNT or ORGANIZATION
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a Analyzer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AnalyzerArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["analyzerName"] = args ? args.analyzerName : undefined;
            resourceInputs["archiveRules"] = args ? args.archiveRules : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["analyzerName"] = undefined /*out*/;
            resourceInputs["archiveRules"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["analyzerName", "type"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Analyzer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Analyzer resource.
 */
export interface AnalyzerArgs {
    /**
     * Analyzer name
     */
    analyzerName?: pulumi.Input<string>;
    archiveRules?: pulumi.Input<pulumi.Input<inputs.accessanalyzer.AnalyzerArchiveRuleArgs>[]>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.accessanalyzer.AnalyzerTagArgs>[]>;
    /**
     * The type of the analyzer, must be ACCOUNT or ORGANIZATION
     */
    type: pulumi.Input<string>;
}
