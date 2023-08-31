// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ses

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SES::ReceiptRule
//
// Deprecated: ReceiptRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ReceiptRule struct {
	pulumi.CustomResourceState

	After       pulumi.StringPtrOutput `pulumi:"after"`
	Rule        ReceiptRuleRuleOutput  `pulumi:"rule"`
	RuleSetName pulumi.StringOutput    `pulumi:"ruleSetName"`
}

// NewReceiptRule registers a new resource with the given unique name, arguments, and options.
func NewReceiptRule(ctx *pulumi.Context,
	name string, args *ReceiptRuleArgs, opts ...pulumi.ResourceOption) (*ReceiptRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Rule == nil {
		return nil, errors.New("invalid value for required argument 'Rule'")
	}
	if args.RuleSetName == nil {
		return nil, errors.New("invalid value for required argument 'RuleSetName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"ruleSetName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ReceiptRule
	err := ctx.RegisterResource("aws-native:ses:ReceiptRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReceiptRule gets an existing ReceiptRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReceiptRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReceiptRuleState, opts ...pulumi.ResourceOption) (*ReceiptRule, error) {
	var resource ReceiptRule
	err := ctx.ReadResource("aws-native:ses:ReceiptRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReceiptRule resources.
type receiptRuleState struct {
}

type ReceiptRuleState struct {
}

func (ReceiptRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*receiptRuleState)(nil)).Elem()
}

type receiptRuleArgs struct {
	After       *string         `pulumi:"after"`
	Rule        ReceiptRuleRule `pulumi:"rule"`
	RuleSetName string          `pulumi:"ruleSetName"`
}

// The set of arguments for constructing a ReceiptRule resource.
type ReceiptRuleArgs struct {
	After       pulumi.StringPtrInput
	Rule        ReceiptRuleRuleInput
	RuleSetName pulumi.StringInput
}

func (ReceiptRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*receiptRuleArgs)(nil)).Elem()
}

type ReceiptRuleInput interface {
	pulumi.Input

	ToReceiptRuleOutput() ReceiptRuleOutput
	ToReceiptRuleOutputWithContext(ctx context.Context) ReceiptRuleOutput
}

func (*ReceiptRule) ElementType() reflect.Type {
	return reflect.TypeOf((**ReceiptRule)(nil)).Elem()
}

func (i *ReceiptRule) ToReceiptRuleOutput() ReceiptRuleOutput {
	return i.ToReceiptRuleOutputWithContext(context.Background())
}

func (i *ReceiptRule) ToReceiptRuleOutputWithContext(ctx context.Context) ReceiptRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReceiptRuleOutput)
}

type ReceiptRuleOutput struct{ *pulumi.OutputState }

func (ReceiptRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ReceiptRule)(nil)).Elem()
}

func (o ReceiptRuleOutput) ToReceiptRuleOutput() ReceiptRuleOutput {
	return o
}

func (o ReceiptRuleOutput) ToReceiptRuleOutputWithContext(ctx context.Context) ReceiptRuleOutput {
	return o
}

func (o ReceiptRuleOutput) After() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ReceiptRule) pulumi.StringPtrOutput { return v.After }).(pulumi.StringPtrOutput)
}

func (o ReceiptRuleOutput) Rule() ReceiptRuleRuleOutput {
	return o.ApplyT(func(v *ReceiptRule) ReceiptRuleRuleOutput { return v.Rule }).(ReceiptRuleRuleOutput)
}

func (o ReceiptRuleOutput) RuleSetName() pulumi.StringOutput {
	return o.ApplyT(func(v *ReceiptRule) pulumi.StringOutput { return v.RuleSetName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ReceiptRuleInput)(nil)).Elem(), &ReceiptRule{})
	pulumi.RegisterOutputType(ReceiptRuleOutput{})
}
