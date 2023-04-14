// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataSync::Task.
 */
export class Task extends pulumi.CustomResource {
    /**
     * Get an existing Task resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Task {
        return new Task(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:datasync:Task';

    /**
     * Returns true if the given object is an instance of Task.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Task {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Task.__pulumiType;
    }

    /**
     * The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
     */
    public readonly cloudWatchLogGroupArn!: pulumi.Output<string | undefined>;
    /**
     * The ARN of an AWS storage resource's location.
     */
    public readonly destinationLocationArn!: pulumi.Output<string>;
    public /*out*/ readonly destinationNetworkInterfaceArns!: pulumi.Output<string[]>;
    public readonly excludes!: pulumi.Output<outputs.datasync.TaskFilterRule[] | undefined>;
    public readonly includes!: pulumi.Output<outputs.datasync.TaskFilterRule[] | undefined>;
    /**
     * The name of a task. This value is a text reference that is used to identify the task in the console.
     */
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly options!: pulumi.Output<outputs.datasync.TaskOptions | undefined>;
    public readonly schedule!: pulumi.Output<outputs.datasync.TaskSchedule | undefined>;
    /**
     * The ARN of the source location for the task.
     */
    public readonly sourceLocationArn!: pulumi.Output<string>;
    public /*out*/ readonly sourceNetworkInterfaceArns!: pulumi.Output<string[]>;
    /**
     * The status of the task that was described.
     */
    public /*out*/ readonly status!: pulumi.Output<enums.datasync.TaskStatus>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.datasync.TaskTag[] | undefined>;
    /**
     * The ARN of the task.
     */
    public /*out*/ readonly taskArn!: pulumi.Output<string>;

    /**
     * Create a Task resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TaskArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.destinationLocationArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'destinationLocationArn'");
            }
            if ((!args || args.sourceLocationArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceLocationArn'");
            }
            resourceInputs["cloudWatchLogGroupArn"] = args ? args.cloudWatchLogGroupArn : undefined;
            resourceInputs["destinationLocationArn"] = args ? args.destinationLocationArn : undefined;
            resourceInputs["excludes"] = args ? args.excludes : undefined;
            resourceInputs["includes"] = args ? args.includes : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["options"] = args ? args.options : undefined;
            resourceInputs["schedule"] = args ? args.schedule : undefined;
            resourceInputs["sourceLocationArn"] = args ? args.sourceLocationArn : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["destinationNetworkInterfaceArns"] = undefined /*out*/;
            resourceInputs["sourceNetworkInterfaceArns"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["taskArn"] = undefined /*out*/;
        } else {
            resourceInputs["cloudWatchLogGroupArn"] = undefined /*out*/;
            resourceInputs["destinationLocationArn"] = undefined /*out*/;
            resourceInputs["destinationNetworkInterfaceArns"] = undefined /*out*/;
            resourceInputs["excludes"] = undefined /*out*/;
            resourceInputs["includes"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["options"] = undefined /*out*/;
            resourceInputs["schedule"] = undefined /*out*/;
            resourceInputs["sourceLocationArn"] = undefined /*out*/;
            resourceInputs["sourceNetworkInterfaceArns"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["taskArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Task.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Task resource.
 */
export interface TaskArgs {
    /**
     * The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
     */
    cloudWatchLogGroupArn?: pulumi.Input<string>;
    /**
     * The ARN of an AWS storage resource's location.
     */
    destinationLocationArn: pulumi.Input<string>;
    excludes?: pulumi.Input<pulumi.Input<inputs.datasync.TaskFilterRuleArgs>[]>;
    includes?: pulumi.Input<pulumi.Input<inputs.datasync.TaskFilterRuleArgs>[]>;
    /**
     * The name of a task. This value is a text reference that is used to identify the task in the console.
     */
    name?: pulumi.Input<string>;
    options?: pulumi.Input<inputs.datasync.TaskOptionsArgs>;
    schedule?: pulumi.Input<inputs.datasync.TaskScheduleArgs>;
    /**
     * The ARN of the source location for the task.
     */
    sourceLocationArn: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.datasync.TaskTagArgs>[]>;
}
