// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataSync::Task.
type Task struct {
	pulumi.CustomResourceState

	// The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
	CloudWatchLogGroupArn pulumi.StringPtrOutput `pulumi:"cloudWatchLogGroupArn"`
	// The ARN of an AWS storage resource's location.
	DestinationLocationArn          pulumi.StringOutput       `pulumi:"destinationLocationArn"`
	DestinationNetworkInterfaceArns pulumi.StringArrayOutput  `pulumi:"destinationNetworkInterfaceArns"`
	Excludes                        TaskFilterRuleArrayOutput `pulumi:"excludes"`
	Includes                        TaskFilterRuleArrayOutput `pulumi:"includes"`
	// The name of a task. This value is a text reference that is used to identify the task in the console.
	Name     pulumi.StringPtrOutput `pulumi:"name"`
	Options  TaskOptionsPtrOutput   `pulumi:"options"`
	Schedule TaskSchedulePtrOutput  `pulumi:"schedule"`
	// The ARN of the source location for the task.
	SourceLocationArn          pulumi.StringOutput      `pulumi:"sourceLocationArn"`
	SourceNetworkInterfaceArns pulumi.StringArrayOutput `pulumi:"sourceNetworkInterfaceArns"`
	// The status of the task that was described.
	Status TaskStatusOutput `pulumi:"status"`
	// An array of key-value pairs to apply to this resource.
	Tags TaskTagArrayOutput `pulumi:"tags"`
	// The ARN of the task.
	TaskArn pulumi.StringOutput `pulumi:"taskArn"`
}

// NewTask registers a new resource with the given unique name, arguments, and options.
func NewTask(ctx *pulumi.Context,
	name string, args *TaskArgs, opts ...pulumi.ResourceOption) (*Task, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DestinationLocationArn == nil {
		return nil, errors.New("invalid value for required argument 'DestinationLocationArn'")
	}
	if args.SourceLocationArn == nil {
		return nil, errors.New("invalid value for required argument 'SourceLocationArn'")
	}
	var resource Task
	err := ctx.RegisterResource("aws-native:datasync:Task", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTask gets an existing Task resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTask(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TaskState, opts ...pulumi.ResourceOption) (*Task, error) {
	var resource Task
	err := ctx.ReadResource("aws-native:datasync:Task", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Task resources.
type taskState struct {
}

type TaskState struct {
}

func (TaskState) ElementType() reflect.Type {
	return reflect.TypeOf((*taskState)(nil)).Elem()
}

type taskArgs struct {
	// The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
	CloudWatchLogGroupArn *string `pulumi:"cloudWatchLogGroupArn"`
	// The ARN of an AWS storage resource's location.
	DestinationLocationArn string           `pulumi:"destinationLocationArn"`
	Excludes               []TaskFilterRule `pulumi:"excludes"`
	Includes               []TaskFilterRule `pulumi:"includes"`
	// The name of a task. This value is a text reference that is used to identify the task in the console.
	Name     *string       `pulumi:"name"`
	Options  *TaskOptions  `pulumi:"options"`
	Schedule *TaskSchedule `pulumi:"schedule"`
	// The ARN of the source location for the task.
	SourceLocationArn string `pulumi:"sourceLocationArn"`
	// An array of key-value pairs to apply to this resource.
	Tags []TaskTag `pulumi:"tags"`
}

// The set of arguments for constructing a Task resource.
type TaskArgs struct {
	// The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
	CloudWatchLogGroupArn pulumi.StringPtrInput
	// The ARN of an AWS storage resource's location.
	DestinationLocationArn pulumi.StringInput
	Excludes               TaskFilterRuleArrayInput
	Includes               TaskFilterRuleArrayInput
	// The name of a task. This value is a text reference that is used to identify the task in the console.
	Name     pulumi.StringPtrInput
	Options  TaskOptionsPtrInput
	Schedule TaskSchedulePtrInput
	// The ARN of the source location for the task.
	SourceLocationArn pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	Tags TaskTagArrayInput
}

func (TaskArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*taskArgs)(nil)).Elem()
}

type TaskInput interface {
	pulumi.Input

	ToTaskOutput() TaskOutput
	ToTaskOutputWithContext(ctx context.Context) TaskOutput
}

func (*Task) ElementType() reflect.Type {
	return reflect.TypeOf((**Task)(nil)).Elem()
}

func (i *Task) ToTaskOutput() TaskOutput {
	return i.ToTaskOutputWithContext(context.Background())
}

func (i *Task) ToTaskOutputWithContext(ctx context.Context) TaskOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TaskOutput)
}

type TaskOutput struct{ *pulumi.OutputState }

func (TaskOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Task)(nil)).Elem()
}

func (o TaskOutput) ToTaskOutput() TaskOutput {
	return o
}

func (o TaskOutput) ToTaskOutputWithContext(ctx context.Context) TaskOutput {
	return o
}

// The ARN of the Amazon CloudWatch log group that is used to monitor and log events in the task.
func (o TaskOutput) CloudWatchLogGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Task) pulumi.StringPtrOutput { return v.CloudWatchLogGroupArn }).(pulumi.StringPtrOutput)
}

// The ARN of an AWS storage resource's location.
func (o TaskOutput) DestinationLocationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Task) pulumi.StringOutput { return v.DestinationLocationArn }).(pulumi.StringOutput)
}

func (o TaskOutput) DestinationNetworkInterfaceArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Task) pulumi.StringArrayOutput { return v.DestinationNetworkInterfaceArns }).(pulumi.StringArrayOutput)
}

func (o TaskOutput) Excludes() TaskFilterRuleArrayOutput {
	return o.ApplyT(func(v *Task) TaskFilterRuleArrayOutput { return v.Excludes }).(TaskFilterRuleArrayOutput)
}

func (o TaskOutput) Includes() TaskFilterRuleArrayOutput {
	return o.ApplyT(func(v *Task) TaskFilterRuleArrayOutput { return v.Includes }).(TaskFilterRuleArrayOutput)
}

// The name of a task. This value is a text reference that is used to identify the task in the console.
func (o TaskOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Task) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o TaskOutput) Options() TaskOptionsPtrOutput {
	return o.ApplyT(func(v *Task) TaskOptionsPtrOutput { return v.Options }).(TaskOptionsPtrOutput)
}

func (o TaskOutput) Schedule() TaskSchedulePtrOutput {
	return o.ApplyT(func(v *Task) TaskSchedulePtrOutput { return v.Schedule }).(TaskSchedulePtrOutput)
}

// The ARN of the source location for the task.
func (o TaskOutput) SourceLocationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Task) pulumi.StringOutput { return v.SourceLocationArn }).(pulumi.StringOutput)
}

func (o TaskOutput) SourceNetworkInterfaceArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Task) pulumi.StringArrayOutput { return v.SourceNetworkInterfaceArns }).(pulumi.StringArrayOutput)
}

// The status of the task that was described.
func (o TaskOutput) Status() TaskStatusOutput {
	return o.ApplyT(func(v *Task) TaskStatusOutput { return v.Status }).(TaskStatusOutput)
}

// An array of key-value pairs to apply to this resource.
func (o TaskOutput) Tags() TaskTagArrayOutput {
	return o.ApplyT(func(v *Task) TaskTagArrayOutput { return v.Tags }).(TaskTagArrayOutput)
}

// The ARN of the task.
func (o TaskOutput) TaskArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Task) pulumi.StringOutput { return v.TaskArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TaskInput)(nil)).Elem(), &Task{})
	pulumi.RegisterOutputType(TaskOutput{})
}
