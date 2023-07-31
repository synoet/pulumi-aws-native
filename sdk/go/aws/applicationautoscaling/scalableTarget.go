// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package applicationautoscaling

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ApplicationAutoScaling::ScalableTarget
type ScalableTarget struct {
	pulumi.CustomResourceState

	// The maximum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
	MaxCapacity pulumi.IntOutput `pulumi:"maxCapacity"`
	// The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
	MinCapacity pulumi.IntOutput `pulumi:"minCapacity"`
	// The identifier of the resource associated with the scalable target
	ResourceId pulumi.StringOutput `pulumi:"resourceId"`
	// Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.
	RoleArn pulumi.StringPtrOutput `pulumi:"roleArn"`
	// The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property
	ScalableDimension pulumi.StringOutput `pulumi:"scalableDimension"`
	// The scheduled actions for the scalable target. Duplicates aren't allowed.
	ScheduledActions ScalableTargetScheduledActionArrayOutput `pulumi:"scheduledActions"`
	// The namespace of the AWS service that provides the resource, or a custom-resource
	ServiceNamespace pulumi.StringOutput `pulumi:"serviceNamespace"`
	// An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.
	SuspendedState ScalableTargetSuspendedStatePtrOutput `pulumi:"suspendedState"`
}

// NewScalableTarget registers a new resource with the given unique name, arguments, and options.
func NewScalableTarget(ctx *pulumi.Context,
	name string, args *ScalableTargetArgs, opts ...pulumi.ResourceOption) (*ScalableTarget, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MaxCapacity == nil {
		return nil, errors.New("invalid value for required argument 'MaxCapacity'")
	}
	if args.MinCapacity == nil {
		return nil, errors.New("invalid value for required argument 'MinCapacity'")
	}
	if args.ResourceId == nil {
		return nil, errors.New("invalid value for required argument 'ResourceId'")
	}
	if args.ScalableDimension == nil {
		return nil, errors.New("invalid value for required argument 'ScalableDimension'")
	}
	if args.ServiceNamespace == nil {
		return nil, errors.New("invalid value for required argument 'ServiceNamespace'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ScalableTarget
	err := ctx.RegisterResource("aws-native:applicationautoscaling:ScalableTarget", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetScalableTarget gets an existing ScalableTarget resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetScalableTarget(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ScalableTargetState, opts ...pulumi.ResourceOption) (*ScalableTarget, error) {
	var resource ScalableTarget
	err := ctx.ReadResource("aws-native:applicationautoscaling:ScalableTarget", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ScalableTarget resources.
type scalableTargetState struct {
}

type ScalableTargetState struct {
}

func (ScalableTargetState) ElementType() reflect.Type {
	return reflect.TypeOf((*scalableTargetState)(nil)).Elem()
}

type scalableTargetArgs struct {
	// The maximum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
	MaxCapacity int `pulumi:"maxCapacity"`
	// The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
	MinCapacity int `pulumi:"minCapacity"`
	// The identifier of the resource associated with the scalable target
	ResourceId string `pulumi:"resourceId"`
	// Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.
	RoleArn *string `pulumi:"roleArn"`
	// The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property
	ScalableDimension string `pulumi:"scalableDimension"`
	// The scheduled actions for the scalable target. Duplicates aren't allowed.
	ScheduledActions []ScalableTargetScheduledAction `pulumi:"scheduledActions"`
	// The namespace of the AWS service that provides the resource, or a custom-resource
	ServiceNamespace string `pulumi:"serviceNamespace"`
	// An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.
	SuspendedState *ScalableTargetSuspendedState `pulumi:"suspendedState"`
}

// The set of arguments for constructing a ScalableTarget resource.
type ScalableTargetArgs struct {
	// The maximum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
	MaxCapacity pulumi.IntInput
	// The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
	MinCapacity pulumi.IntInput
	// The identifier of the resource associated with the scalable target
	ResourceId pulumi.StringInput
	// Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.
	RoleArn pulumi.StringPtrInput
	// The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property
	ScalableDimension pulumi.StringInput
	// The scheduled actions for the scalable target. Duplicates aren't allowed.
	ScheduledActions ScalableTargetScheduledActionArrayInput
	// The namespace of the AWS service that provides the resource, or a custom-resource
	ServiceNamespace pulumi.StringInput
	// An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.
	SuspendedState ScalableTargetSuspendedStatePtrInput
}

func (ScalableTargetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*scalableTargetArgs)(nil)).Elem()
}

type ScalableTargetInput interface {
	pulumi.Input

	ToScalableTargetOutput() ScalableTargetOutput
	ToScalableTargetOutputWithContext(ctx context.Context) ScalableTargetOutput
}

func (*ScalableTarget) ElementType() reflect.Type {
	return reflect.TypeOf((**ScalableTarget)(nil)).Elem()
}

func (i *ScalableTarget) ToScalableTargetOutput() ScalableTargetOutput {
	return i.ToScalableTargetOutputWithContext(context.Background())
}

func (i *ScalableTarget) ToScalableTargetOutputWithContext(ctx context.Context) ScalableTargetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScalableTargetOutput)
}

type ScalableTargetOutput struct{ *pulumi.OutputState }

func (ScalableTargetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ScalableTarget)(nil)).Elem()
}

func (o ScalableTargetOutput) ToScalableTargetOutput() ScalableTargetOutput {
	return o
}

func (o ScalableTargetOutput) ToScalableTargetOutputWithContext(ctx context.Context) ScalableTargetOutput {
	return o
}

// The maximum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
func (o ScalableTargetOutput) MaxCapacity() pulumi.IntOutput {
	return o.ApplyT(func(v *ScalableTarget) pulumi.IntOutput { return v.MaxCapacity }).(pulumi.IntOutput)
}

// The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand
func (o ScalableTargetOutput) MinCapacity() pulumi.IntOutput {
	return o.ApplyT(func(v *ScalableTarget) pulumi.IntOutput { return v.MinCapacity }).(pulumi.IntOutput)
}

// The identifier of the resource associated with the scalable target
func (o ScalableTargetOutput) ResourceId() pulumi.StringOutput {
	return o.ApplyT(func(v *ScalableTarget) pulumi.StringOutput { return v.ResourceId }).(pulumi.StringOutput)
}

// Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf.
func (o ScalableTargetOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ScalableTarget) pulumi.StringPtrOutput { return v.RoleArn }).(pulumi.StringPtrOutput)
}

// The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property
func (o ScalableTargetOutput) ScalableDimension() pulumi.StringOutput {
	return o.ApplyT(func(v *ScalableTarget) pulumi.StringOutput { return v.ScalableDimension }).(pulumi.StringOutput)
}

// The scheduled actions for the scalable target. Duplicates aren't allowed.
func (o ScalableTargetOutput) ScheduledActions() ScalableTargetScheduledActionArrayOutput {
	return o.ApplyT(func(v *ScalableTarget) ScalableTargetScheduledActionArrayOutput { return v.ScheduledActions }).(ScalableTargetScheduledActionArrayOutput)
}

// The namespace of the AWS service that provides the resource, or a custom-resource
func (o ScalableTargetOutput) ServiceNamespace() pulumi.StringOutput {
	return o.ApplyT(func(v *ScalableTarget) pulumi.StringOutput { return v.ServiceNamespace }).(pulumi.StringOutput)
}

// An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.
func (o ScalableTargetOutput) SuspendedState() ScalableTargetSuspendedStatePtrOutput {
	return o.ApplyT(func(v *ScalableTarget) ScalableTargetSuspendedStatePtrOutput { return v.SuspendedState }).(ScalableTargetSuspendedStatePtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ScalableTargetInput)(nil)).Elem(), &ScalableTarget{})
	pulumi.RegisterOutputType(ScalableTargetOutput{})
}
