# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetAlarmResult',
    'AwaitableGetAlarmResult',
    'get_alarm',
    'get_alarm_output',
]

@pulumi.output_type
class GetAlarmResult:
    def __init__(__self__, actions_enabled=None, alarm_actions=None, alarm_description=None, arn=None, comparison_operator=None, datapoints_to_alarm=None, dimensions=None, evaluate_low_sample_count_percentile=None, evaluation_periods=None, extended_statistic=None, insufficient_data_actions=None, metric_name=None, metrics=None, namespace=None, ok_actions=None, period=None, statistic=None, threshold=None, threshold_metric_id=None, treat_missing_data=None, unit=None):
        if actions_enabled and not isinstance(actions_enabled, bool):
            raise TypeError("Expected argument 'actions_enabled' to be a bool")
        pulumi.set(__self__, "actions_enabled", actions_enabled)
        if alarm_actions and not isinstance(alarm_actions, list):
            raise TypeError("Expected argument 'alarm_actions' to be a list")
        pulumi.set(__self__, "alarm_actions", alarm_actions)
        if alarm_description and not isinstance(alarm_description, str):
            raise TypeError("Expected argument 'alarm_description' to be a str")
        pulumi.set(__self__, "alarm_description", alarm_description)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if comparison_operator and not isinstance(comparison_operator, str):
            raise TypeError("Expected argument 'comparison_operator' to be a str")
        pulumi.set(__self__, "comparison_operator", comparison_operator)
        if datapoints_to_alarm and not isinstance(datapoints_to_alarm, int):
            raise TypeError("Expected argument 'datapoints_to_alarm' to be a int")
        pulumi.set(__self__, "datapoints_to_alarm", datapoints_to_alarm)
        if dimensions and not isinstance(dimensions, list):
            raise TypeError("Expected argument 'dimensions' to be a list")
        pulumi.set(__self__, "dimensions", dimensions)
        if evaluate_low_sample_count_percentile and not isinstance(evaluate_low_sample_count_percentile, str):
            raise TypeError("Expected argument 'evaluate_low_sample_count_percentile' to be a str")
        pulumi.set(__self__, "evaluate_low_sample_count_percentile", evaluate_low_sample_count_percentile)
        if evaluation_periods and not isinstance(evaluation_periods, int):
            raise TypeError("Expected argument 'evaluation_periods' to be a int")
        pulumi.set(__self__, "evaluation_periods", evaluation_periods)
        if extended_statistic and not isinstance(extended_statistic, str):
            raise TypeError("Expected argument 'extended_statistic' to be a str")
        pulumi.set(__self__, "extended_statistic", extended_statistic)
        if insufficient_data_actions and not isinstance(insufficient_data_actions, list):
            raise TypeError("Expected argument 'insufficient_data_actions' to be a list")
        pulumi.set(__self__, "insufficient_data_actions", insufficient_data_actions)
        if metric_name and not isinstance(metric_name, str):
            raise TypeError("Expected argument 'metric_name' to be a str")
        pulumi.set(__self__, "metric_name", metric_name)
        if metrics and not isinstance(metrics, list):
            raise TypeError("Expected argument 'metrics' to be a list")
        pulumi.set(__self__, "metrics", metrics)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if ok_actions and not isinstance(ok_actions, list):
            raise TypeError("Expected argument 'ok_actions' to be a list")
        pulumi.set(__self__, "ok_actions", ok_actions)
        if period and not isinstance(period, int):
            raise TypeError("Expected argument 'period' to be a int")
        pulumi.set(__self__, "period", period)
        if statistic and not isinstance(statistic, str):
            raise TypeError("Expected argument 'statistic' to be a str")
        pulumi.set(__self__, "statistic", statistic)
        if threshold and not isinstance(threshold, float):
            raise TypeError("Expected argument 'threshold' to be a float")
        pulumi.set(__self__, "threshold", threshold)
        if threshold_metric_id and not isinstance(threshold_metric_id, str):
            raise TypeError("Expected argument 'threshold_metric_id' to be a str")
        pulumi.set(__self__, "threshold_metric_id", threshold_metric_id)
        if treat_missing_data and not isinstance(treat_missing_data, str):
            raise TypeError("Expected argument 'treat_missing_data' to be a str")
        pulumi.set(__self__, "treat_missing_data", treat_missing_data)
        if unit and not isinstance(unit, str):
            raise TypeError("Expected argument 'unit' to be a str")
        pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="actionsEnabled")
    def actions_enabled(self) -> Optional[bool]:
        """
        Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        """
        return pulumi.get(self, "actions_enabled")

    @property
    @pulumi.getter(name="alarmActions")
    def alarm_actions(self) -> Optional[Sequence[str]]:
        """
        The list of actions to execute when this alarm transitions into an ALARM state from any other state.
        """
        return pulumi.get(self, "alarm_actions")

    @property
    @pulumi.getter(name="alarmDescription")
    def alarm_description(self) -> Optional[str]:
        """
        The description of the alarm.
        """
        return pulumi.get(self, "alarm_description")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name is a unique name for each resource.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        The arithmetic operation to use when comparing the specified statistic and threshold.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter(name="datapointsToAlarm")
    def datapoints_to_alarm(self) -> Optional[int]:
        """
        The number of datapoints that must be breaching to trigger the alarm.
        """
        return pulumi.get(self, "datapoints_to_alarm")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.AlarmDimension']]:
        """
        The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="evaluateLowSampleCountPercentile")
    def evaluate_low_sample_count_percentile(self) -> Optional[str]:
        """
        Used only for alarms based on percentiles.
        """
        return pulumi.get(self, "evaluate_low_sample_count_percentile")

    @property
    @pulumi.getter(name="evaluationPeriods")
    def evaluation_periods(self) -> Optional[int]:
        """
        The number of periods over which data is compared to the specified threshold.
        """
        return pulumi.get(self, "evaluation_periods")

    @property
    @pulumi.getter(name="extendedStatistic")
    def extended_statistic(self) -> Optional[str]:
        """
        The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        """
        return pulumi.get(self, "extended_statistic")

    @property
    @pulumi.getter(name="insufficientDataActions")
    def insufficient_data_actions(self) -> Optional[Sequence[str]]:
        """
        The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.
        """
        return pulumi.get(self, "insufficient_data_actions")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[str]:
        """
        The name of the metric associated with the alarm.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def metrics(self) -> Optional[Sequence['outputs.AlarmMetricDataQuery']]:
        """
        An array that enables you to create an alarm based on the result of a metric math expression.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The namespace of the metric associated with the alarm.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="okActions")
    def ok_actions(self) -> Optional[Sequence[str]]:
        """
        The actions to execute when this alarm transitions to the OK state from any other state.
        """
        return pulumi.get(self, "ok_actions")

    @property
    @pulumi.getter
    def period(self) -> Optional[int]:
        """
        The period in seconds, over which the statistic is applied.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter
    def statistic(self) -> Optional[str]:
        """
        The statistic for the metric associated with the alarm, other than percentile.
        """
        return pulumi.get(self, "statistic")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[float]:
        """
        In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter(name="thresholdMetricId")
    def threshold_metric_id(self) -> Optional[str]:
        """
        In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        """
        return pulumi.get(self, "threshold_metric_id")

    @property
    @pulumi.getter(name="treatMissingData")
    def treat_missing_data(self) -> Optional[str]:
        """
        Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.
        """
        return pulumi.get(self, "treat_missing_data")

    @property
    @pulumi.getter
    def unit(self) -> Optional[str]:
        """
        The unit of the metric associated with the alarm.
        """
        return pulumi.get(self, "unit")


class AwaitableGetAlarmResult(GetAlarmResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAlarmResult(
            actions_enabled=self.actions_enabled,
            alarm_actions=self.alarm_actions,
            alarm_description=self.alarm_description,
            arn=self.arn,
            comparison_operator=self.comparison_operator,
            datapoints_to_alarm=self.datapoints_to_alarm,
            dimensions=self.dimensions,
            evaluate_low_sample_count_percentile=self.evaluate_low_sample_count_percentile,
            evaluation_periods=self.evaluation_periods,
            extended_statistic=self.extended_statistic,
            insufficient_data_actions=self.insufficient_data_actions,
            metric_name=self.metric_name,
            metrics=self.metrics,
            namespace=self.namespace,
            ok_actions=self.ok_actions,
            period=self.period,
            statistic=self.statistic,
            threshold=self.threshold,
            threshold_metric_id=self.threshold_metric_id,
            treat_missing_data=self.treat_missing_data,
            unit=self.unit)


def get_alarm(alarm_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAlarmResult:
    """
    Resource Type definition for AWS::CloudWatch::Alarm


    :param str alarm_name: The name of the alarm.
    """
    __args__ = dict()
    __args__['alarmName'] = alarm_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudwatch:getAlarm', __args__, opts=opts, typ=GetAlarmResult).value

    return AwaitableGetAlarmResult(
        actions_enabled=pulumi.get(__ret__, 'actions_enabled'),
        alarm_actions=pulumi.get(__ret__, 'alarm_actions'),
        alarm_description=pulumi.get(__ret__, 'alarm_description'),
        arn=pulumi.get(__ret__, 'arn'),
        comparison_operator=pulumi.get(__ret__, 'comparison_operator'),
        datapoints_to_alarm=pulumi.get(__ret__, 'datapoints_to_alarm'),
        dimensions=pulumi.get(__ret__, 'dimensions'),
        evaluate_low_sample_count_percentile=pulumi.get(__ret__, 'evaluate_low_sample_count_percentile'),
        evaluation_periods=pulumi.get(__ret__, 'evaluation_periods'),
        extended_statistic=pulumi.get(__ret__, 'extended_statistic'),
        insufficient_data_actions=pulumi.get(__ret__, 'insufficient_data_actions'),
        metric_name=pulumi.get(__ret__, 'metric_name'),
        metrics=pulumi.get(__ret__, 'metrics'),
        namespace=pulumi.get(__ret__, 'namespace'),
        ok_actions=pulumi.get(__ret__, 'ok_actions'),
        period=pulumi.get(__ret__, 'period'),
        statistic=pulumi.get(__ret__, 'statistic'),
        threshold=pulumi.get(__ret__, 'threshold'),
        threshold_metric_id=pulumi.get(__ret__, 'threshold_metric_id'),
        treat_missing_data=pulumi.get(__ret__, 'treat_missing_data'),
        unit=pulumi.get(__ret__, 'unit'))


@_utilities.lift_output_func(get_alarm)
def get_alarm_output(alarm_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAlarmResult]:
    """
    Resource Type definition for AWS::CloudWatch::Alarm


    :param str alarm_name: The name of the alarm.
    """
    ...
