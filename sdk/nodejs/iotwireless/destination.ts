// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Destination's resource schema demonstrating some basic constructs and validation rules.
 */
export class Destination extends pulumi.CustomResource {
    /**
     * Get an existing Destination resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Destination {
        return new Destination(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:iotwireless:Destination';

    /**
     * Returns true if the given object is an instance of Destination.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Destination {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Destination.__pulumiType;
    }

    /**
     * Destination arn. Returned after successful create.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * Destination description
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Destination expression
     */
    public readonly expression!: pulumi.Output<string>;
    /**
     * Must be RuleName
     */
    public readonly expressionType!: pulumi.Output<enums.iotwireless.DestinationExpressionType>;
    /**
     * Unique name of destination
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * AWS role ARN that grants access
     */
    public readonly roleArn!: pulumi.Output<string>;
    /**
     * A list of key-value pairs that contain metadata for the destination.
     */
    public readonly tags!: pulumi.Output<outputs.iotwireless.DestinationTag[] | undefined>;

    /**
     * Create a Destination resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DestinationArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.expression === undefined) && !opts.urn) {
                throw new Error("Missing required property 'expression'");
            }
            if ((!args || args.expressionType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'expressionType'");
            }
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["expression"] = args ? args.expression : undefined;
            inputs["expressionType"] = args ? args.expressionType : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["expression"] = undefined /*out*/;
            inputs["expressionType"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["roleArn"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Destination.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Destination resource.
 */
export interface DestinationArgs {
    /**
     * Destination description
     */
    description?: pulumi.Input<string>;
    /**
     * Destination expression
     */
    expression: pulumi.Input<string>;
    /**
     * Must be RuleName
     */
    expressionType: pulumi.Input<enums.iotwireless.DestinationExpressionType>;
    /**
     * Unique name of destination
     */
    name?: pulumi.Input<string>;
    /**
     * AWS role ARN that grants access
     */
    roleArn: pulumi.Input<string>;
    /**
     * A list of key-value pairs that contain metadata for the destination.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.iotwireless.DestinationTagArgs>[]>;
}
