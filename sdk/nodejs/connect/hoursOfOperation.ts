// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::HoursOfOperation
 */
export class HoursOfOperation extends pulumi.CustomResource {
    /**
     * Get an existing HoursOfOperation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): HoursOfOperation {
        return new HoursOfOperation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:connect:HoursOfOperation';

    /**
     * Returns true if the given object is an instance of HoursOfOperation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is HoursOfOperation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === HoursOfOperation.__pulumiType;
    }

    /**
     * Configuration information for the hours of operation: day, start time, and end time.
     */
    public readonly config!: pulumi.Output<outputs.connect.HoursOfOperationConfig[]>;
    /**
     * The description of the hours of operation.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) for the hours of operation.
     */
    public /*out*/ readonly hoursOfOperationArn!: pulumi.Output<string>;
    /**
     * The identifier of the Amazon Connect instance.
     */
    public readonly instanceArn!: pulumi.Output<string>;
    /**
     * The name of the hours of operation.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * One or more tags.
     */
    public readonly tags!: pulumi.Output<outputs.connect.HoursOfOperationTag[] | undefined>;
    /**
     * The time zone of the hours of operation.
     */
    public readonly timeZone!: pulumi.Output<string>;

    /**
     * Create a HoursOfOperation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: HoursOfOperationArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.config === undefined) && !opts.urn) {
                throw new Error("Missing required property 'config'");
            }
            if ((!args || args.instanceArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceArn'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.timeZone === undefined) && !opts.urn) {
                throw new Error("Missing required property 'timeZone'");
            }
            inputs["config"] = args ? args.config : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["instanceArn"] = args ? args.instanceArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["timeZone"] = args ? args.timeZone : undefined;
            inputs["hoursOfOperationArn"] = undefined /*out*/;
        } else {
            inputs["config"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["hoursOfOperationArn"] = undefined /*out*/;
            inputs["instanceArn"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["timeZone"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(HoursOfOperation.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a HoursOfOperation resource.
 */
export interface HoursOfOperationArgs {
    /**
     * Configuration information for the hours of operation: day, start time, and end time.
     */
    config: pulumi.Input<pulumi.Input<inputs.connect.HoursOfOperationConfigArgs>[]>;
    /**
     * The description of the hours of operation.
     */
    description?: pulumi.Input<string>;
    /**
     * The identifier of the Amazon Connect instance.
     */
    instanceArn: pulumi.Input<string>;
    /**
     * The name of the hours of operation.
     */
    name: pulumi.Input<string>;
    /**
     * One or more tags.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.connect.HoursOfOperationTagArgs>[]>;
    /**
     * The time zone of the hours of operation.
     */
    timeZone: pulumi.Input<string>;
}
