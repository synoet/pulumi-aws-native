// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.
 */
export class ScheduledAction extends pulumi.CustomResource {
    /**
     * Get an existing ScheduledAction resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ScheduledAction {
        return new ScheduledAction(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:autoscaling:ScheduledAction';

    /**
     * Returns true if the given object is an instance of ScheduledAction.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ScheduledAction {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ScheduledAction.__pulumiType;
    }

    /**
     * The name of the Auto Scaling group.
     */
    public readonly autoScalingGroupName!: pulumi.Output<string>;
    /**
     * The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
     */
    public readonly desiredCapacity!: pulumi.Output<number | undefined>;
    /**
     * The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
     */
    public readonly endTime!: pulumi.Output<string | undefined>;
    /**
     * The minimum size of the Auto Scaling group.
     */
    public readonly maxSize!: pulumi.Output<number | undefined>;
    /**
     * The minimum size of the Auto Scaling group.
     */
    public readonly minSize!: pulumi.Output<number | undefined>;
    /**
     * The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
     */
    public readonly recurrence!: pulumi.Output<string | undefined>;
    /**
     * Auto-generated unique identifier
     */
    public /*out*/ readonly scheduledActionName!: pulumi.Output<string>;
    /**
     * The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
     */
    public readonly startTime!: pulumi.Output<string | undefined>;
    /**
     * The time zone for the cron expression.
     */
    public readonly timeZone!: pulumi.Output<string | undefined>;

    /**
     * Create a ScheduledAction resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ScheduledActionArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.autoScalingGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'autoScalingGroupName'");
            }
            resourceInputs["autoScalingGroupName"] = args ? args.autoScalingGroupName : undefined;
            resourceInputs["desiredCapacity"] = args ? args.desiredCapacity : undefined;
            resourceInputs["endTime"] = args ? args.endTime : undefined;
            resourceInputs["maxSize"] = args ? args.maxSize : undefined;
            resourceInputs["minSize"] = args ? args.minSize : undefined;
            resourceInputs["recurrence"] = args ? args.recurrence : undefined;
            resourceInputs["startTime"] = args ? args.startTime : undefined;
            resourceInputs["timeZone"] = args ? args.timeZone : undefined;
            resourceInputs["scheduledActionName"] = undefined /*out*/;
        } else {
            resourceInputs["autoScalingGroupName"] = undefined /*out*/;
            resourceInputs["desiredCapacity"] = undefined /*out*/;
            resourceInputs["endTime"] = undefined /*out*/;
            resourceInputs["maxSize"] = undefined /*out*/;
            resourceInputs["minSize"] = undefined /*out*/;
            resourceInputs["recurrence"] = undefined /*out*/;
            resourceInputs["scheduledActionName"] = undefined /*out*/;
            resourceInputs["startTime"] = undefined /*out*/;
            resourceInputs["timeZone"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["autoScalingGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ScheduledAction.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ScheduledAction resource.
 */
export interface ScheduledActionArgs {
    /**
     * The name of the Auto Scaling group.
     */
    autoScalingGroupName: pulumi.Input<string>;
    /**
     * The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
     */
    desiredCapacity?: pulumi.Input<number>;
    /**
     * The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
     */
    endTime?: pulumi.Input<string>;
    /**
     * The minimum size of the Auto Scaling group.
     */
    maxSize?: pulumi.Input<number>;
    /**
     * The minimum size of the Auto Scaling group.
     */
    minSize?: pulumi.Input<number>;
    /**
     * The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
     */
    recurrence?: pulumi.Input<string>;
    /**
     * The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
     */
    startTime?: pulumi.Input<string>;
    /**
     * The time zone for the cron expression.
     */
    timeZone?: pulumi.Input<string>;
}
