// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::CloudFormation::Stack resource nests a stack as a resource in a top-level template.
type Stack struct {
	pulumi.CustomResourceState

	Capabilities                StackCapabilitiesItemArrayOutput `pulumi:"capabilities"`
	ChangeSetId                 pulumi.StringOutput              `pulumi:"changeSetId"`
	CreationTime                pulumi.StringOutput              `pulumi:"creationTime"`
	Description                 pulumi.StringPtrOutput           `pulumi:"description"`
	DisableRollback             pulumi.BoolPtrOutput             `pulumi:"disableRollback"`
	EnableTerminationProtection pulumi.BoolPtrOutput             `pulumi:"enableTerminationProtection"`
	LastUpdateTime              pulumi.StringOutput              `pulumi:"lastUpdateTime"`
	NotificationArns            pulumi.StringArrayOutput         `pulumi:"notificationArns"`
	Outputs                     StackOutputTypeArrayOutput       `pulumi:"outputs"`
	Parameters                  pulumi.AnyOutput                 `pulumi:"parameters"`
	ParentId                    pulumi.StringOutput              `pulumi:"parentId"`
	RoleArn                     pulumi.StringPtrOutput           `pulumi:"roleArn"`
	RootId                      pulumi.StringOutput              `pulumi:"rootId"`
	StackId                     pulumi.StringOutput              `pulumi:"stackId"`
	StackName                   pulumi.StringOutput              `pulumi:"stackName"`
	StackPolicyBody             pulumi.AnyOutput                 `pulumi:"stackPolicyBody"`
	StackPolicyUrl              pulumi.StringPtrOutput           `pulumi:"stackPolicyUrl"`
	StackStatus                 StackStatusOutput                `pulumi:"stackStatus"`
	StackStatusReason           pulumi.StringPtrOutput           `pulumi:"stackStatusReason"`
	Tags                        StackTagArrayOutput              `pulumi:"tags"`
	TemplateBody                pulumi.AnyOutput                 `pulumi:"templateBody"`
	TemplateUrl                 pulumi.StringPtrOutput           `pulumi:"templateUrl"`
	TimeoutInMinutes            pulumi.IntPtrOutput              `pulumi:"timeoutInMinutes"`
}

// NewStack registers a new resource with the given unique name, arguments, and options.
func NewStack(ctx *pulumi.Context,
	name string, args *StackArgs, opts ...pulumi.ResourceOption) (*Stack, error) {
	if args == nil {
		args = &StackArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"stackName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Stack
	err := ctx.RegisterResource("aws-native:cloudformation:Stack", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStack gets an existing Stack resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStack(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StackState, opts ...pulumi.ResourceOption) (*Stack, error) {
	var resource Stack
	err := ctx.ReadResource("aws-native:cloudformation:Stack", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Stack resources.
type stackState struct {
}

type StackState struct {
}

func (StackState) ElementType() reflect.Type {
	return reflect.TypeOf((*stackState)(nil)).Elem()
}

type stackArgs struct {
	Capabilities                []StackCapabilitiesItem `pulumi:"capabilities"`
	Description                 *string                 `pulumi:"description"`
	DisableRollback             *bool                   `pulumi:"disableRollback"`
	EnableTerminationProtection *bool                   `pulumi:"enableTerminationProtection"`
	NotificationArns            []string                `pulumi:"notificationArns"`
	Parameters                  interface{}             `pulumi:"parameters"`
	RoleArn                     *string                 `pulumi:"roleArn"`
	StackName                   *string                 `pulumi:"stackName"`
	StackPolicyBody             interface{}             `pulumi:"stackPolicyBody"`
	StackPolicyUrl              *string                 `pulumi:"stackPolicyUrl"`
	StackStatusReason           *string                 `pulumi:"stackStatusReason"`
	Tags                        []StackTag              `pulumi:"tags"`
	TemplateBody                interface{}             `pulumi:"templateBody"`
	TemplateUrl                 *string                 `pulumi:"templateUrl"`
	TimeoutInMinutes            *int                    `pulumi:"timeoutInMinutes"`
}

// The set of arguments for constructing a Stack resource.
type StackArgs struct {
	Capabilities                StackCapabilitiesItemArrayInput
	Description                 pulumi.StringPtrInput
	DisableRollback             pulumi.BoolPtrInput
	EnableTerminationProtection pulumi.BoolPtrInput
	NotificationArns            pulumi.StringArrayInput
	Parameters                  pulumi.Input
	RoleArn                     pulumi.StringPtrInput
	StackName                   pulumi.StringPtrInput
	StackPolicyBody             pulumi.Input
	StackPolicyUrl              pulumi.StringPtrInput
	StackStatusReason           pulumi.StringPtrInput
	Tags                        StackTagArrayInput
	TemplateBody                pulumi.Input
	TemplateUrl                 pulumi.StringPtrInput
	TimeoutInMinutes            pulumi.IntPtrInput
}

func (StackArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stackArgs)(nil)).Elem()
}

type StackInput interface {
	pulumi.Input

	ToStackOutput() StackOutput
	ToStackOutputWithContext(ctx context.Context) StackOutput
}

func (*Stack) ElementType() reflect.Type {
	return reflect.TypeOf((**Stack)(nil)).Elem()
}

func (i *Stack) ToStackOutput() StackOutput {
	return i.ToStackOutputWithContext(context.Background())
}

func (i *Stack) ToStackOutputWithContext(ctx context.Context) StackOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackOutput)
}

type StackOutput struct{ *pulumi.OutputState }

func (StackOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Stack)(nil)).Elem()
}

func (o StackOutput) ToStackOutput() StackOutput {
	return o
}

func (o StackOutput) ToStackOutputWithContext(ctx context.Context) StackOutput {
	return o
}

func (o StackOutput) Capabilities() StackCapabilitiesItemArrayOutput {
	return o.ApplyT(func(v *Stack) StackCapabilitiesItemArrayOutput { return v.Capabilities }).(StackCapabilitiesItemArrayOutput)
}

func (o StackOutput) ChangeSetId() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.ChangeSetId }).(pulumi.StringOutput)
}

func (o StackOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

func (o StackOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o StackOutput) DisableRollback() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.BoolPtrOutput { return v.DisableRollback }).(pulumi.BoolPtrOutput)
}

func (o StackOutput) EnableTerminationProtection() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.BoolPtrOutput { return v.EnableTerminationProtection }).(pulumi.BoolPtrOutput)
}

func (o StackOutput) LastUpdateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.LastUpdateTime }).(pulumi.StringOutput)
}

func (o StackOutput) NotificationArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringArrayOutput { return v.NotificationArns }).(pulumi.StringArrayOutput)
}

func (o StackOutput) Outputs() StackOutputTypeArrayOutput {
	return o.ApplyT(func(v *Stack) StackOutputTypeArrayOutput { return v.Outputs }).(StackOutputTypeArrayOutput)
}

func (o StackOutput) Parameters() pulumi.AnyOutput {
	return o.ApplyT(func(v *Stack) pulumi.AnyOutput { return v.Parameters }).(pulumi.AnyOutput)
}

func (o StackOutput) ParentId() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.ParentId }).(pulumi.StringOutput)
}

func (o StackOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o StackOutput) RootId() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.RootId }).(pulumi.StringOutput)
}

func (o StackOutput) StackId() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.StackId }).(pulumi.StringOutput)
}

func (o StackOutput) StackName() pulumi.StringOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringOutput { return v.StackName }).(pulumi.StringOutput)
}

func (o StackOutput) StackPolicyBody() pulumi.AnyOutput {
	return o.ApplyT(func(v *Stack) pulumi.AnyOutput { return v.StackPolicyBody }).(pulumi.AnyOutput)
}

func (o StackOutput) StackPolicyUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.StackPolicyUrl }).(pulumi.StringPtrOutput)
}

func (o StackOutput) StackStatus() StackStatusOutput {
	return o.ApplyT(func(v *Stack) StackStatusOutput { return v.StackStatus }).(StackStatusOutput)
}

func (o StackOutput) StackStatusReason() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.StackStatusReason }).(pulumi.StringPtrOutput)
}

func (o StackOutput) Tags() StackTagArrayOutput {
	return o.ApplyT(func(v *Stack) StackTagArrayOutput { return v.Tags }).(StackTagArrayOutput)
}

func (o StackOutput) TemplateBody() pulumi.AnyOutput {
	return o.ApplyT(func(v *Stack) pulumi.AnyOutput { return v.TemplateBody }).(pulumi.AnyOutput)
}

func (o StackOutput) TemplateUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.StringPtrOutput { return v.TemplateUrl }).(pulumi.StringPtrOutput)
}

func (o StackOutput) TimeoutInMinutes() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Stack) pulumi.IntPtrOutput { return v.TimeoutInMinutes }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StackInput)(nil)).Elem(), &Stack{})
	pulumi.RegisterOutputType(StackOutput{})
}
