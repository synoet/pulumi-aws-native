// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::ImageBuilder::InfrastructureConfiguration
 */
export class InfrastructureConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing InfrastructureConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): InfrastructureConfiguration {
        return new InfrastructureConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:imagebuilder:InfrastructureConfiguration';

    /**
     * Returns true if the given object is an instance of InfrastructureConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is InfrastructureConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === InfrastructureConfiguration.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the infrastructure configuration.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The description of the infrastructure configuration.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The instance profile of the infrastructure configuration.
     */
    public readonly instanceProfileName!: pulumi.Output<string>;
    /**
     * The instance types of the infrastructure configuration.
     */
    public readonly instanceTypes!: pulumi.Output<string[] | undefined>;
    /**
     * The EC2 key pair of the infrastructure configuration..
     */
    public readonly keyPair!: pulumi.Output<string | undefined>;
    /**
     * The logging configuration of the infrastructure configuration.
     */
    public readonly logging!: pulumi.Output<outputs.imagebuilder.InfrastructureConfigurationLogging | undefined>;
    /**
     * The name of the infrastructure configuration.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The tags attached to the resource created by Image Builder.
     */
    public readonly resourceTags!: pulumi.Output<any | undefined>;
    /**
     * The security group IDs of the infrastructure configuration.
     */
    public readonly securityGroupIds!: pulumi.Output<string[] | undefined>;
    /**
     * The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
     */
    public readonly snsTopicArn!: pulumi.Output<string | undefined>;
    /**
     * The subnet ID of the infrastructure configuration.
     */
    public readonly subnetId!: pulumi.Output<string | undefined>;
    /**
     * The tags associated with the component.
     */
    public readonly tags!: pulumi.Output<any | undefined>;
    /**
     * The terminate instance on failure configuration of the infrastructure configuration.
     */
    public readonly terminateInstanceOnFailure!: pulumi.Output<boolean | undefined>;

    /**
     * Create a InfrastructureConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InfrastructureConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceProfileName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceProfileName'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["instanceProfileName"] = args ? args.instanceProfileName : undefined;
            inputs["instanceTypes"] = args ? args.instanceTypes : undefined;
            inputs["keyPair"] = args ? args.keyPair : undefined;
            inputs["logging"] = args ? args.logging : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["resourceTags"] = args ? args.resourceTags : undefined;
            inputs["securityGroupIds"] = args ? args.securityGroupIds : undefined;
            inputs["snsTopicArn"] = args ? args.snsTopicArn : undefined;
            inputs["subnetId"] = args ? args.subnetId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["terminateInstanceOnFailure"] = args ? args.terminateInstanceOnFailure : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["instanceProfileName"] = undefined /*out*/;
            inputs["instanceTypes"] = undefined /*out*/;
            inputs["keyPair"] = undefined /*out*/;
            inputs["logging"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["resourceTags"] = undefined /*out*/;
            inputs["securityGroupIds"] = undefined /*out*/;
            inputs["snsTopicArn"] = undefined /*out*/;
            inputs["subnetId"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["terminateInstanceOnFailure"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(InfrastructureConfiguration.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a InfrastructureConfiguration resource.
 */
export interface InfrastructureConfigurationArgs {
    /**
     * The description of the infrastructure configuration.
     */
    description?: pulumi.Input<string>;
    /**
     * The instance profile of the infrastructure configuration.
     */
    instanceProfileName: pulumi.Input<string>;
    /**
     * The instance types of the infrastructure configuration.
     */
    instanceTypes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The EC2 key pair of the infrastructure configuration..
     */
    keyPair?: pulumi.Input<string>;
    /**
     * The logging configuration of the infrastructure configuration.
     */
    logging?: pulumi.Input<inputs.imagebuilder.InfrastructureConfigurationLoggingArgs>;
    /**
     * The name of the infrastructure configuration.
     */
    name: pulumi.Input<string>;
    /**
     * The tags attached to the resource created by Image Builder.
     */
    resourceTags?: any;
    /**
     * The security group IDs of the infrastructure configuration.
     */
    securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The SNS Topic Amazon Resource Name (ARN) of the infrastructure configuration.
     */
    snsTopicArn?: pulumi.Input<string>;
    /**
     * The subnet ID of the infrastructure configuration.
     */
    subnetId?: pulumi.Input<string>;
    /**
     * The tags associated with the component.
     */
    tags?: any;
    /**
     * The terminate instance on failure configuration of the infrastructure configuration.
     */
    terminateInstanceOnFailure?: pulumi.Input<boolean>;
}
