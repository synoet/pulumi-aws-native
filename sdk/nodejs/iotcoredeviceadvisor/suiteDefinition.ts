// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html
 */
export class SuiteDefinition extends pulumi.CustomResource {
    /**
     * Get an existing SuiteDefinition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SuiteDefinition {
        return new SuiteDefinition(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotcoredeviceadvisor:SuiteDefinition';

    /**
     * Returns true if the given object is an instance of SuiteDefinition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SuiteDefinition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SuiteDefinition.__pulumiType;
    }

    public /*out*/ readonly suiteDefinitionArn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
     */
    public readonly suiteDefinitionConfiguration!: pulumi.Output<any | string>;
    public /*out*/ readonly suiteDefinitionId!: pulumi.Output<string>;
    public /*out*/ readonly suiteDefinitionVersion!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a SuiteDefinition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SuiteDefinitionArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.suiteDefinitionConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'suiteDefinitionConfiguration'");
            }
            inputs["suiteDefinitionConfiguration"] = args ? args.suiteDefinitionConfiguration : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["suiteDefinitionArn"] = undefined /*out*/;
            inputs["suiteDefinitionId"] = undefined /*out*/;
            inputs["suiteDefinitionVersion"] = undefined /*out*/;
        } else {
            inputs["suiteDefinitionArn"] = undefined /*out*/;
            inputs["suiteDefinitionConfiguration"] = undefined /*out*/;
            inputs["suiteDefinitionId"] = undefined /*out*/;
            inputs["suiteDefinitionVersion"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(SuiteDefinition.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a SuiteDefinition resource.
 */
export interface SuiteDefinitionArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
     */
    suiteDefinitionConfiguration: pulumi.Input<any | string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
