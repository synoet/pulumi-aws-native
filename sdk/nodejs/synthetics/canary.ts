// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Synthetics::Canary
 */
export class Canary extends pulumi.CustomResource {
    /**
     * Get an existing Canary resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Canary {
        return new Canary(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:synthetics:Canary';

    /**
     * Returns true if the given object is an instance of Canary.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Canary {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Canary.__pulumiType;
    }

    /**
     * Provide the s3 bucket output location for test results
     */
    public readonly artifactS3Location!: pulumi.Output<string>;
    /**
     * Provide the canary script source
     */
    public readonly code!: pulumi.Output<outputs.synthetics.CanaryCode>;
    /**
     * Lambda Execution role used to run your canaries
     */
    public readonly executionRoleArn!: pulumi.Output<string>;
    /**
     * Retention period of failed canary runs represented in number of days
     */
    public readonly failureRetentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * Name of the canary.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Provide canary run configuration
     */
    public readonly runConfig!: pulumi.Output<outputs.synthetics.CanaryRunConfig | undefined>;
    /**
     * Runtime version of Synthetics Library
     */
    public readonly runtimeVersion!: pulumi.Output<string>;
    /**
     * Frequency to run your canaries
     */
    public readonly schedule!: pulumi.Output<outputs.synthetics.CanarySchedule>;
    /**
     * Runs canary if set to True. Default is False
     */
    public readonly startCanaryAfterCreation!: pulumi.Output<boolean>;
    /**
     * State of the canary
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * Retention period of successful canary runs represented in number of days
     */
    public readonly successRetentionPeriod!: pulumi.Output<number | undefined>;
    public readonly tags!: pulumi.Output<outputs.synthetics.CanaryTag[] | undefined>;
    /**
     * Provide VPC Configuration if enabled.
     */
    public readonly vPCConfig!: pulumi.Output<outputs.synthetics.CanaryVPCConfig | undefined>;
    /**
     * Visual reference configuration for visual testing
     */
    public readonly visualReference!: pulumi.Output<outputs.synthetics.CanaryVisualReference | undefined>;

    /**
     * Create a Canary resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CanaryArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.artifactS3Location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'artifactS3Location'");
            }
            if ((!args || args.code === undefined) && !opts.urn) {
                throw new Error("Missing required property 'code'");
            }
            if ((!args || args.executionRoleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'executionRoleArn'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.runtimeVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'runtimeVersion'");
            }
            if ((!args || args.schedule === undefined) && !opts.urn) {
                throw new Error("Missing required property 'schedule'");
            }
            if ((!args || args.startCanaryAfterCreation === undefined) && !opts.urn) {
                throw new Error("Missing required property 'startCanaryAfterCreation'");
            }
            inputs["artifactS3Location"] = args ? args.artifactS3Location : undefined;
            inputs["code"] = args ? args.code : undefined;
            inputs["executionRoleArn"] = args ? args.executionRoleArn : undefined;
            inputs["failureRetentionPeriod"] = args ? args.failureRetentionPeriod : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["runConfig"] = args ? args.runConfig : undefined;
            inputs["runtimeVersion"] = args ? args.runtimeVersion : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
            inputs["startCanaryAfterCreation"] = args ? args.startCanaryAfterCreation : undefined;
            inputs["successRetentionPeriod"] = args ? args.successRetentionPeriod : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vPCConfig"] = args ? args.vPCConfig : undefined;
            inputs["visualReference"] = args ? args.visualReference : undefined;
            inputs["state"] = undefined /*out*/;
        } else {
            inputs["artifactS3Location"] = undefined /*out*/;
            inputs["code"] = undefined /*out*/;
            inputs["executionRoleArn"] = undefined /*out*/;
            inputs["failureRetentionPeriod"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["runConfig"] = undefined /*out*/;
            inputs["runtimeVersion"] = undefined /*out*/;
            inputs["schedule"] = undefined /*out*/;
            inputs["startCanaryAfterCreation"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["successRetentionPeriod"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["vPCConfig"] = undefined /*out*/;
            inputs["visualReference"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Canary.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Canary resource.
 */
export interface CanaryArgs {
    /**
     * Provide the s3 bucket output location for test results
     */
    artifactS3Location: pulumi.Input<string>;
    /**
     * Provide the canary script source
     */
    code: pulumi.Input<inputs.synthetics.CanaryCodeArgs>;
    /**
     * Lambda Execution role used to run your canaries
     */
    executionRoleArn: pulumi.Input<string>;
    /**
     * Retention period of failed canary runs represented in number of days
     */
    failureRetentionPeriod?: pulumi.Input<number>;
    /**
     * Name of the canary.
     */
    name: pulumi.Input<string>;
    /**
     * Provide canary run configuration
     */
    runConfig?: pulumi.Input<inputs.synthetics.CanaryRunConfigArgs>;
    /**
     * Runtime version of Synthetics Library
     */
    runtimeVersion: pulumi.Input<string>;
    /**
     * Frequency to run your canaries
     */
    schedule: pulumi.Input<inputs.synthetics.CanaryScheduleArgs>;
    /**
     * Runs canary if set to True. Default is False
     */
    startCanaryAfterCreation: pulumi.Input<boolean>;
    /**
     * Retention period of successful canary runs represented in number of days
     */
    successRetentionPeriod?: pulumi.Input<number>;
    tags?: pulumi.Input<pulumi.Input<inputs.synthetics.CanaryTagArgs>[]>;
    /**
     * Provide VPC Configuration if enabled.
     */
    vPCConfig?: pulumi.Input<inputs.synthetics.CanaryVPCConfigArgs>;
    /**
     * Visual reference configuration for visual testing
     */
    visualReference?: pulumi.Input<inputs.synthetics.CanaryVisualReferenceArgs>;
}
