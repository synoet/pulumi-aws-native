// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stepfunctions

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for StateMachineVersion
type StateMachineVersion struct {
	pulumi.CustomResourceState

	Arn                    pulumi.StringOutput    `pulumi:"arn"`
	Description            pulumi.StringPtrOutput `pulumi:"description"`
	StateMachineArn        pulumi.StringOutput    `pulumi:"stateMachineArn"`
	StateMachineRevisionId pulumi.StringPtrOutput `pulumi:"stateMachineRevisionId"`
}

// NewStateMachineVersion registers a new resource with the given unique name, arguments, and options.
func NewStateMachineVersion(ctx *pulumi.Context,
	name string, args *StateMachineVersionArgs, opts ...pulumi.ResourceOption) (*StateMachineVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.StateMachineArn == nil {
		return nil, errors.New("invalid value for required argument 'StateMachineArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"stateMachineArn",
		"stateMachineRevisionId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StateMachineVersion
	err := ctx.RegisterResource("aws-native:stepfunctions:StateMachineVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStateMachineVersion gets an existing StateMachineVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStateMachineVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StateMachineVersionState, opts ...pulumi.ResourceOption) (*StateMachineVersion, error) {
	var resource StateMachineVersion
	err := ctx.ReadResource("aws-native:stepfunctions:StateMachineVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StateMachineVersion resources.
type stateMachineVersionState struct {
}

type StateMachineVersionState struct {
}

func (StateMachineVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineVersionState)(nil)).Elem()
}

type stateMachineVersionArgs struct {
	Description            *string `pulumi:"description"`
	StateMachineArn        string  `pulumi:"stateMachineArn"`
	StateMachineRevisionId *string `pulumi:"stateMachineRevisionId"`
}

// The set of arguments for constructing a StateMachineVersion resource.
type StateMachineVersionArgs struct {
	Description            pulumi.StringPtrInput
	StateMachineArn        pulumi.StringInput
	StateMachineRevisionId pulumi.StringPtrInput
}

func (StateMachineVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stateMachineVersionArgs)(nil)).Elem()
}

type StateMachineVersionInput interface {
	pulumi.Input

	ToStateMachineVersionOutput() StateMachineVersionOutput
	ToStateMachineVersionOutputWithContext(ctx context.Context) StateMachineVersionOutput
}

func (*StateMachineVersion) ElementType() reflect.Type {
	return reflect.TypeOf((**StateMachineVersion)(nil)).Elem()
}

func (i *StateMachineVersion) ToStateMachineVersionOutput() StateMachineVersionOutput {
	return i.ToStateMachineVersionOutputWithContext(context.Background())
}

func (i *StateMachineVersion) ToStateMachineVersionOutputWithContext(ctx context.Context) StateMachineVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StateMachineVersionOutput)
}

type StateMachineVersionOutput struct{ *pulumi.OutputState }

func (StateMachineVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StateMachineVersion)(nil)).Elem()
}

func (o StateMachineVersionOutput) ToStateMachineVersionOutput() StateMachineVersionOutput {
	return o
}

func (o StateMachineVersionOutput) ToStateMachineVersionOutputWithContext(ctx context.Context) StateMachineVersionOutput {
	return o
}

func (o StateMachineVersionOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachineVersion) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o StateMachineVersionOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StateMachineVersion) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o StateMachineVersionOutput) StateMachineArn() pulumi.StringOutput {
	return o.ApplyT(func(v *StateMachineVersion) pulumi.StringOutput { return v.StateMachineArn }).(pulumi.StringOutput)
}

func (o StateMachineVersionOutput) StateMachineRevisionId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StateMachineVersion) pulumi.StringPtrOutput { return v.StateMachineRevisionId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StateMachineVersionInput)(nil)).Elem(), &StateMachineVersion{})
	pulumi.RegisterOutputType(StateMachineVersionOutput{})
}
