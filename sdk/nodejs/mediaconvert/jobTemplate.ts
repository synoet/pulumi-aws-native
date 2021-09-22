// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MediaConvert::JobTemplate
 *
 * @deprecated JobTemplate is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class JobTemplate extends pulumi.CustomResource {
    /**
     * Get an existing JobTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): JobTemplate {
        pulumi.log.warn("JobTemplate is deprecated: JobTemplate is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new JobTemplate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediaconvert:JobTemplate';

    /**
     * Returns true if the given object is an instance of JobTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is JobTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === JobTemplate.__pulumiType;
    }

    public readonly accelerationSettings!: pulumi.Output<outputs.mediaconvert.JobTemplateAccelerationSettings | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly category!: pulumi.Output<string | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly hopDestinations!: pulumi.Output<outputs.mediaconvert.JobTemplateHopDestination[] | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly priority!: pulumi.Output<number | undefined>;
    public readonly queue!: pulumi.Output<string | undefined>;
    public readonly settingsJson!: pulumi.Output<any>;
    public readonly statusUpdateInterval!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<any | undefined>;

    /**
     * Create a JobTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated JobTemplate is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: JobTemplateArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("JobTemplate is deprecated: JobTemplate is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.settingsJson === undefined) && !opts.urn) {
                throw new Error("Missing required property 'settingsJson'");
            }
            inputs["accelerationSettings"] = args ? args.accelerationSettings : undefined;
            inputs["category"] = args ? args.category : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["hopDestinations"] = args ? args.hopDestinations : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["priority"] = args ? args.priority : undefined;
            inputs["queue"] = args ? args.queue : undefined;
            inputs["settingsJson"] = args ? args.settingsJson : undefined;
            inputs["statusUpdateInterval"] = args ? args.statusUpdateInterval : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["accelerationSettings"] = undefined /*out*/;
            inputs["arn"] = undefined /*out*/;
            inputs["category"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["hopDestinations"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["priority"] = undefined /*out*/;
            inputs["queue"] = undefined /*out*/;
            inputs["settingsJson"] = undefined /*out*/;
            inputs["statusUpdateInterval"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(JobTemplate.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a JobTemplate resource.
 */
export interface JobTemplateArgs {
    accelerationSettings?: pulumi.Input<inputs.mediaconvert.JobTemplateAccelerationSettingsArgs>;
    category?: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    hopDestinations?: pulumi.Input<pulumi.Input<inputs.mediaconvert.JobTemplateHopDestinationArgs>[]>;
    name?: pulumi.Input<string>;
    priority?: pulumi.Input<number>;
    queue?: pulumi.Input<string>;
    settingsJson: any;
    statusUpdateInterval?: pulumi.Input<string>;
    tags?: any;
}
