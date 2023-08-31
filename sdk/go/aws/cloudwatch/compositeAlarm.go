// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::CloudWatch::CompositeAlarm type specifies an alarm which aggregates the states of other Alarms (Metric or Composite Alarms) as defined by the AlarmRule expression
type CompositeAlarm struct {
	pulumi.CustomResourceState

	// Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
	ActionsEnabled pulumi.BoolPtrOutput `pulumi:"actionsEnabled"`
	// Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
	ActionsSuppressor pulumi.StringPtrOutput `pulumi:"actionsSuppressor"`
	// Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.
	ActionsSuppressorExtensionPeriod pulumi.IntPtrOutput `pulumi:"actionsSuppressorExtensionPeriod"`
	// Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.
	ActionsSuppressorWaitPeriod pulumi.IntPtrOutput `pulumi:"actionsSuppressorWaitPeriod"`
	// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
	AlarmActions pulumi.StringArrayOutput `pulumi:"alarmActions"`
	// The description of the alarm
	AlarmDescription pulumi.StringPtrOutput `pulumi:"alarmDescription"`
	// The name of the Composite Alarm
	AlarmName pulumi.StringPtrOutput `pulumi:"alarmName"`
	// Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
	AlarmRule pulumi.StringOutput `pulumi:"alarmRule"`
	// Amazon Resource Name (ARN) of the alarm
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
	InsufficientDataActions pulumi.StringArrayOutput `pulumi:"insufficientDataActions"`
	// The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
	OkActions pulumi.StringArrayOutput `pulumi:"okActions"`
}

// NewCompositeAlarm registers a new resource with the given unique name, arguments, and options.
func NewCompositeAlarm(ctx *pulumi.Context,
	name string, args *CompositeAlarmArgs, opts ...pulumi.ResourceOption) (*CompositeAlarm, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AlarmRule == nil {
		return nil, errors.New("invalid value for required argument 'AlarmRule'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"alarmName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CompositeAlarm
	err := ctx.RegisterResource("aws-native:cloudwatch:CompositeAlarm", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCompositeAlarm gets an existing CompositeAlarm resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCompositeAlarm(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CompositeAlarmState, opts ...pulumi.ResourceOption) (*CompositeAlarm, error) {
	var resource CompositeAlarm
	err := ctx.ReadResource("aws-native:cloudwatch:CompositeAlarm", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CompositeAlarm resources.
type compositeAlarmState struct {
}

type CompositeAlarmState struct {
}

func (CompositeAlarmState) ElementType() reflect.Type {
	return reflect.TypeOf((*compositeAlarmState)(nil)).Elem()
}

type compositeAlarmArgs struct {
	// Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
	ActionsEnabled *bool `pulumi:"actionsEnabled"`
	// Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
	ActionsSuppressor *string `pulumi:"actionsSuppressor"`
	// Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.
	ActionsSuppressorExtensionPeriod *int `pulumi:"actionsSuppressorExtensionPeriod"`
	// Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.
	ActionsSuppressorWaitPeriod *int `pulumi:"actionsSuppressorWaitPeriod"`
	// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
	AlarmActions []string `pulumi:"alarmActions"`
	// The description of the alarm
	AlarmDescription *string `pulumi:"alarmDescription"`
	// The name of the Composite Alarm
	AlarmName *string `pulumi:"alarmName"`
	// Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
	AlarmRule string `pulumi:"alarmRule"`
	// The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
	InsufficientDataActions []string `pulumi:"insufficientDataActions"`
	// The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
	OkActions []string `pulumi:"okActions"`
}

// The set of arguments for constructing a CompositeAlarm resource.
type CompositeAlarmArgs struct {
	// Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
	ActionsEnabled pulumi.BoolPtrInput
	// Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
	ActionsSuppressor pulumi.StringPtrInput
	// Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.
	ActionsSuppressorExtensionPeriod pulumi.IntPtrInput
	// Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.
	ActionsSuppressorWaitPeriod pulumi.IntPtrInput
	// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
	AlarmActions pulumi.StringArrayInput
	// The description of the alarm
	AlarmDescription pulumi.StringPtrInput
	// The name of the Composite Alarm
	AlarmName pulumi.StringPtrInput
	// Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
	AlarmRule pulumi.StringInput
	// The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
	InsufficientDataActions pulumi.StringArrayInput
	// The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
	OkActions pulumi.StringArrayInput
}

func (CompositeAlarmArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*compositeAlarmArgs)(nil)).Elem()
}

type CompositeAlarmInput interface {
	pulumi.Input

	ToCompositeAlarmOutput() CompositeAlarmOutput
	ToCompositeAlarmOutputWithContext(ctx context.Context) CompositeAlarmOutput
}

func (*CompositeAlarm) ElementType() reflect.Type {
	return reflect.TypeOf((**CompositeAlarm)(nil)).Elem()
}

func (i *CompositeAlarm) ToCompositeAlarmOutput() CompositeAlarmOutput {
	return i.ToCompositeAlarmOutputWithContext(context.Background())
}

func (i *CompositeAlarm) ToCompositeAlarmOutputWithContext(ctx context.Context) CompositeAlarmOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CompositeAlarmOutput)
}

type CompositeAlarmOutput struct{ *pulumi.OutputState }

func (CompositeAlarmOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CompositeAlarm)(nil)).Elem()
}

func (o CompositeAlarmOutput) ToCompositeAlarmOutput() CompositeAlarmOutput {
	return o
}

func (o CompositeAlarmOutput) ToCompositeAlarmOutputWithContext(ctx context.Context) CompositeAlarmOutput {
	return o
}

// Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
func (o CompositeAlarmOutput) ActionsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.BoolPtrOutput { return v.ActionsEnabled }).(pulumi.BoolPtrOutput)
}

// Actions will be suppressed if the suppressor alarm is in the ALARM state. ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.
func (o CompositeAlarmOutput) ActionsSuppressor() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringPtrOutput { return v.ActionsSuppressor }).(pulumi.StringPtrOutput)
}

// Actions will be suppressed if WaitPeriod is active. The length of time that actions are suppressed is in seconds.
func (o CompositeAlarmOutput) ActionsSuppressorExtensionPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.IntPtrOutput { return v.ActionsSuppressorExtensionPeriod }).(pulumi.IntPtrOutput)
}

// Actions will be suppressed if ExtensionPeriod is active. The length of time that actions are suppressed is in seconds.
func (o CompositeAlarmOutput) ActionsSuppressorWaitPeriod() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.IntPtrOutput { return v.ActionsSuppressorWaitPeriod }).(pulumi.IntPtrOutput)
}

// The list of actions to execute when this alarm transitions into an ALARM state from any other state. Specify each action as an Amazon Resource Name (ARN).
func (o CompositeAlarmOutput) AlarmActions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringArrayOutput { return v.AlarmActions }).(pulumi.StringArrayOutput)
}

// The description of the alarm
func (o CompositeAlarmOutput) AlarmDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringPtrOutput { return v.AlarmDescription }).(pulumi.StringPtrOutput)
}

// The name of the Composite Alarm
func (o CompositeAlarmOutput) AlarmName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringPtrOutput { return v.AlarmName }).(pulumi.StringPtrOutput)
}

// Expression which aggregates the state of other Alarms (Metric or Composite Alarms)
func (o CompositeAlarmOutput) AlarmRule() pulumi.StringOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringOutput { return v.AlarmRule }).(pulumi.StringOutput)
}

// Amazon Resource Name (ARN) of the alarm
func (o CompositeAlarmOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state. Each action is specified as an Amazon Resource Name (ARN).
func (o CompositeAlarmOutput) InsufficientDataActions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringArrayOutput { return v.InsufficientDataActions }).(pulumi.StringArrayOutput)
}

// The actions to execute when this alarm transitions to the OK state from any other state. Each action is specified as an Amazon Resource Name (ARN).
func (o CompositeAlarmOutput) OkActions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CompositeAlarm) pulumi.StringArrayOutput { return v.OkActions }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CompositeAlarmInput)(nil)).Elem(), &CompositeAlarm{})
	pulumi.RegisterOutputType(CompositeAlarmOutput{})
}
