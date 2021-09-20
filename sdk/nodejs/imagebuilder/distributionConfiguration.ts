// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::ImageBuilder::DistributionConfiguration
 */
export class DistributionConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing DistributionConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DistributionConfiguration {
        return new DistributionConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:imagebuilder:DistributionConfiguration';

    /**
     * Returns true if the given object is an instance of DistributionConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DistributionConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DistributionConfiguration.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the distribution configuration.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The description of the distribution configuration.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The distributions of the distribution configuration.
     */
    public readonly distributions!: pulumi.Output<outputs.imagebuilder.DistributionConfigurationDistribution[]>;
    /**
     * The name of the distribution configuration.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The tags associated with the component.
     */
    public readonly tags!: pulumi.Output<any | undefined>;

    /**
     * Create a DistributionConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DistributionConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.distributions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'distributions'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["distributions"] = args ? args.distributions : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["distributions"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DistributionConfiguration.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a DistributionConfiguration resource.
 */
export interface DistributionConfigurationArgs {
    /**
     * The description of the distribution configuration.
     */
    description?: pulumi.Input<string>;
    /**
     * The distributions of the distribution configuration.
     */
    distributions: pulumi.Input<pulumi.Input<inputs.imagebuilder.DistributionConfigurationDistributionArgs>[]>;
    /**
     * The name of the distribution configuration.
     */
    name: pulumi.Input<string>;
    /**
     * The tags associated with the component.
     */
    tags?: any;
}
