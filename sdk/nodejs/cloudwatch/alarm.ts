// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudWatch::Alarm
 *
 * @deprecated Alarm is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Alarm extends pulumi.CustomResource {
    /**
     * Get an existing Alarm resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Alarm {
        pulumi.log.warn("Alarm is deprecated: Alarm is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Alarm(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cloudwatch:Alarm';

    /**
     * Returns true if the given object is an instance of Alarm.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Alarm {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Alarm.__pulumiType;
    }

    public readonly actionsEnabled!: pulumi.Output<boolean | undefined>;
    public readonly alarmActions!: pulumi.Output<string[] | undefined>;
    public readonly alarmDescription!: pulumi.Output<string | undefined>;
    public readonly alarmName!: pulumi.Output<string | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly comparisonOperator!: pulumi.Output<string>;
    public readonly datapointsToAlarm!: pulumi.Output<number | undefined>;
    public readonly dimensions!: pulumi.Output<outputs.cloudwatch.AlarmDimension[] | undefined>;
    public readonly evaluateLowSampleCountPercentile!: pulumi.Output<string | undefined>;
    public readonly evaluationPeriods!: pulumi.Output<number>;
    public readonly extendedStatistic!: pulumi.Output<string | undefined>;
    public readonly insufficientDataActions!: pulumi.Output<string[] | undefined>;
    public readonly metricName!: pulumi.Output<string | undefined>;
    public readonly metrics!: pulumi.Output<outputs.cloudwatch.AlarmMetricDataQuery[] | undefined>;
    public readonly namespace!: pulumi.Output<string | undefined>;
    public readonly okActions!: pulumi.Output<string[] | undefined>;
    public readonly period!: pulumi.Output<number | undefined>;
    public readonly statistic!: pulumi.Output<string | undefined>;
    public readonly threshold!: pulumi.Output<number | undefined>;
    public readonly thresholdMetricId!: pulumi.Output<string | undefined>;
    public readonly treatMissingData!: pulumi.Output<string | undefined>;
    public readonly unit!: pulumi.Output<string | undefined>;

    /**
     * Create a Alarm resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Alarm is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: AlarmArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Alarm is deprecated: Alarm is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.comparisonOperator === undefined) && !opts.urn) {
                throw new Error("Missing required property 'comparisonOperator'");
            }
            if ((!args || args.evaluationPeriods === undefined) && !opts.urn) {
                throw new Error("Missing required property 'evaluationPeriods'");
            }
            resourceInputs["actionsEnabled"] = args ? args.actionsEnabled : undefined;
            resourceInputs["alarmActions"] = args ? args.alarmActions : undefined;
            resourceInputs["alarmDescription"] = args ? args.alarmDescription : undefined;
            resourceInputs["alarmName"] = args ? args.alarmName : undefined;
            resourceInputs["comparisonOperator"] = args ? args.comparisonOperator : undefined;
            resourceInputs["datapointsToAlarm"] = args ? args.datapointsToAlarm : undefined;
            resourceInputs["dimensions"] = args ? args.dimensions : undefined;
            resourceInputs["evaluateLowSampleCountPercentile"] = args ? args.evaluateLowSampleCountPercentile : undefined;
            resourceInputs["evaluationPeriods"] = args ? args.evaluationPeriods : undefined;
            resourceInputs["extendedStatistic"] = args ? args.extendedStatistic : undefined;
            resourceInputs["insufficientDataActions"] = args ? args.insufficientDataActions : undefined;
            resourceInputs["metricName"] = args ? args.metricName : undefined;
            resourceInputs["metrics"] = args ? args.metrics : undefined;
            resourceInputs["namespace"] = args ? args.namespace : undefined;
            resourceInputs["okActions"] = args ? args.okActions : undefined;
            resourceInputs["period"] = args ? args.period : undefined;
            resourceInputs["statistic"] = args ? args.statistic : undefined;
            resourceInputs["threshold"] = args ? args.threshold : undefined;
            resourceInputs["thresholdMetricId"] = args ? args.thresholdMetricId : undefined;
            resourceInputs["treatMissingData"] = args ? args.treatMissingData : undefined;
            resourceInputs["unit"] = args ? args.unit : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["actionsEnabled"] = undefined /*out*/;
            resourceInputs["alarmActions"] = undefined /*out*/;
            resourceInputs["alarmDescription"] = undefined /*out*/;
            resourceInputs["alarmName"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["comparisonOperator"] = undefined /*out*/;
            resourceInputs["datapointsToAlarm"] = undefined /*out*/;
            resourceInputs["dimensions"] = undefined /*out*/;
            resourceInputs["evaluateLowSampleCountPercentile"] = undefined /*out*/;
            resourceInputs["evaluationPeriods"] = undefined /*out*/;
            resourceInputs["extendedStatistic"] = undefined /*out*/;
            resourceInputs["insufficientDataActions"] = undefined /*out*/;
            resourceInputs["metricName"] = undefined /*out*/;
            resourceInputs["metrics"] = undefined /*out*/;
            resourceInputs["namespace"] = undefined /*out*/;
            resourceInputs["okActions"] = undefined /*out*/;
            resourceInputs["period"] = undefined /*out*/;
            resourceInputs["statistic"] = undefined /*out*/;
            resourceInputs["threshold"] = undefined /*out*/;
            resourceInputs["thresholdMetricId"] = undefined /*out*/;
            resourceInputs["treatMissingData"] = undefined /*out*/;
            resourceInputs["unit"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Alarm.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Alarm resource.
 */
export interface AlarmArgs {
    actionsEnabled?: pulumi.Input<boolean>;
    alarmActions?: pulumi.Input<pulumi.Input<string>[]>;
    alarmDescription?: pulumi.Input<string>;
    alarmName?: pulumi.Input<string>;
    comparisonOperator: pulumi.Input<string>;
    datapointsToAlarm?: pulumi.Input<number>;
    dimensions?: pulumi.Input<pulumi.Input<inputs.cloudwatch.AlarmDimensionArgs>[]>;
    evaluateLowSampleCountPercentile?: pulumi.Input<string>;
    evaluationPeriods: pulumi.Input<number>;
    extendedStatistic?: pulumi.Input<string>;
    insufficientDataActions?: pulumi.Input<pulumi.Input<string>[]>;
    metricName?: pulumi.Input<string>;
    metrics?: pulumi.Input<pulumi.Input<inputs.cloudwatch.AlarmMetricDataQueryArgs>[]>;
    namespace?: pulumi.Input<string>;
    okActions?: pulumi.Input<pulumi.Input<string>[]>;
    period?: pulumi.Input<number>;
    statistic?: pulumi.Input<string>;
    threshold?: pulumi.Input<number>;
    thresholdMetricId?: pulumi.Input<string>;
    treatMissingData?: pulumi.Input<string>;
    unit?: pulumi.Input<string>;
}
