// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html
 */
export class CodeSigningConfig extends pulumi.CustomResource {
    /**
     * Get an existing CodeSigningConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): CodeSigningConfig {
        return new CodeSigningConfig(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:lambda:CodeSigningConfig';

    /**
     * Returns true if the given object is an instance of CodeSigningConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CodeSigningConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CodeSigningConfig.__pulumiType;
    }

    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers
     */
    public readonly allowedPublishers!: pulumi.Output<outputs.lambda.CodeSigningConfigAllowedPublishers>;
    public /*out*/ readonly codeSigningConfigArn!: pulumi.Output<string>;
    public /*out*/ readonly codeSigningConfigId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies
     */
    public readonly codeSigningPolicies!: pulumi.Output<outputs.lambda.CodeSigningConfigCodeSigningPolicies | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description
     */
    public readonly description!: pulumi.Output<string | undefined>;

    /**
     * Create a CodeSigningConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CodeSigningConfigArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.allowedPublishers === undefined) && !opts.urn) {
                throw new Error("Missing required property 'allowedPublishers'");
            }
            inputs["allowedPublishers"] = args ? args.allowedPublishers : undefined;
            inputs["codeSigningPolicies"] = args ? args.codeSigningPolicies : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["codeSigningConfigArn"] = undefined /*out*/;
            inputs["codeSigningConfigId"] = undefined /*out*/;
        } else {
            inputs["allowedPublishers"] = undefined /*out*/;
            inputs["codeSigningConfigArn"] = undefined /*out*/;
            inputs["codeSigningConfigId"] = undefined /*out*/;
            inputs["codeSigningPolicies"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(CodeSigningConfig.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a CodeSigningConfig resource.
 */
export interface CodeSigningConfigArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-allowedpublishers
     */
    allowedPublishers: pulumi.Input<inputs.lambda.CodeSigningConfigAllowedPublishersArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-codesigningpolicies
     */
    codeSigningPolicies?: pulumi.Input<inputs.lambda.CodeSigningConfigCodeSigningPoliciesArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html#cfn-lambda-codesigningconfig-description
     */
    description?: pulumi.Input<string>;
}
