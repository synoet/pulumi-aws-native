// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package billingconductor

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// A custom line item is an one time charge that is applied to a specific billing group's bill.
//
// Deprecated: CustomLineItem is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type CustomLineItem struct {
	pulumi.CustomResourceState

	// The account which this custom line item will be charged to
	AccountId pulumi.StringPtrOutput `pulumi:"accountId"`
	// ARN
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Number of source values associated to this custom line item
	AssociationSize pulumi.IntOutput `pulumi:"associationSize"`
	// Billing Group ARN
	BillingGroupArn    pulumi.StringOutput                       `pulumi:"billingGroupArn"`
	BillingPeriodRange CustomLineItemBillingPeriodRangePtrOutput `pulumi:"billingPeriodRange"`
	// Creation timestamp in UNIX epoch time format
	CreationTime                pulumi.IntOutput                     `pulumi:"creationTime"`
	CurrencyCode                CustomLineItemCurrencyCodeOutput     `pulumi:"currencyCode"`
	CustomLineItemChargeDetails CustomLineItemChargeDetailsPtrOutput `pulumi:"customLineItemChargeDetails"`
	Description                 pulumi.StringPtrOutput               `pulumi:"description"`
	// Latest modified timestamp in UNIX epoch time format
	LastModifiedTime pulumi.IntOutput             `pulumi:"lastModifiedTime"`
	Name             pulumi.StringOutput          `pulumi:"name"`
	ProductCode      pulumi.StringOutput          `pulumi:"productCode"`
	Tags             CustomLineItemTagArrayOutput `pulumi:"tags"`
}

// NewCustomLineItem registers a new resource with the given unique name, arguments, and options.
func NewCustomLineItem(ctx *pulumi.Context,
	name string, args *CustomLineItemArgs, opts ...pulumi.ResourceOption) (*CustomLineItem, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BillingGroupArn == nil {
		return nil, errors.New("invalid value for required argument 'BillingGroupArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"accountId",
		"billingGroupArn",
		"billingPeriodRange.exclusiveEndBillingPeriod",
		"billingPeriodRange.inclusiveStartBillingPeriod",
		"customLineItemChargeDetails.type",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CustomLineItem
	err := ctx.RegisterResource("aws-native:billingconductor:CustomLineItem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCustomLineItem gets an existing CustomLineItem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCustomLineItem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CustomLineItemState, opts ...pulumi.ResourceOption) (*CustomLineItem, error) {
	var resource CustomLineItem
	err := ctx.ReadResource("aws-native:billingconductor:CustomLineItem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CustomLineItem resources.
type customLineItemState struct {
}

type CustomLineItemState struct {
}

func (CustomLineItemState) ElementType() reflect.Type {
	return reflect.TypeOf((*customLineItemState)(nil)).Elem()
}

type customLineItemArgs struct {
	// The account which this custom line item will be charged to
	AccountId *string `pulumi:"accountId"`
	// Billing Group ARN
	BillingGroupArn             string                            `pulumi:"billingGroupArn"`
	BillingPeriodRange          *CustomLineItemBillingPeriodRange `pulumi:"billingPeriodRange"`
	CustomLineItemChargeDetails *CustomLineItemChargeDetails      `pulumi:"customLineItemChargeDetails"`
	Description                 *string                           `pulumi:"description"`
	Name                        *string                           `pulumi:"name"`
	Tags                        []CustomLineItemTag               `pulumi:"tags"`
}

// The set of arguments for constructing a CustomLineItem resource.
type CustomLineItemArgs struct {
	// The account which this custom line item will be charged to
	AccountId pulumi.StringPtrInput
	// Billing Group ARN
	BillingGroupArn             pulumi.StringInput
	BillingPeriodRange          CustomLineItemBillingPeriodRangePtrInput
	CustomLineItemChargeDetails CustomLineItemChargeDetailsPtrInput
	Description                 pulumi.StringPtrInput
	Name                        pulumi.StringPtrInput
	Tags                        CustomLineItemTagArrayInput
}

func (CustomLineItemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*customLineItemArgs)(nil)).Elem()
}

type CustomLineItemInput interface {
	pulumi.Input

	ToCustomLineItemOutput() CustomLineItemOutput
	ToCustomLineItemOutputWithContext(ctx context.Context) CustomLineItemOutput
}

func (*CustomLineItem) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomLineItem)(nil)).Elem()
}

func (i *CustomLineItem) ToCustomLineItemOutput() CustomLineItemOutput {
	return i.ToCustomLineItemOutputWithContext(context.Background())
}

func (i *CustomLineItem) ToCustomLineItemOutputWithContext(ctx context.Context) CustomLineItemOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CustomLineItemOutput)
}

func (i *CustomLineItem) ToOutput(ctx context.Context) pulumix.Output[*CustomLineItem] {
	return pulumix.Output[*CustomLineItem]{
		OutputState: i.ToCustomLineItemOutputWithContext(ctx).OutputState,
	}
}

type CustomLineItemOutput struct{ *pulumi.OutputState }

func (CustomLineItemOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CustomLineItem)(nil)).Elem()
}

func (o CustomLineItemOutput) ToCustomLineItemOutput() CustomLineItemOutput {
	return o
}

func (o CustomLineItemOutput) ToCustomLineItemOutputWithContext(ctx context.Context) CustomLineItemOutput {
	return o
}

func (o CustomLineItemOutput) ToOutput(ctx context.Context) pulumix.Output[*CustomLineItem] {
	return pulumix.Output[*CustomLineItem]{
		OutputState: o.OutputState,
	}
}

// The account which this custom line item will be charged to
func (o CustomLineItemOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.StringPtrOutput { return v.AccountId }).(pulumi.StringPtrOutput)
}

// ARN
func (o CustomLineItemOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Number of source values associated to this custom line item
func (o CustomLineItemOutput) AssociationSize() pulumi.IntOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.IntOutput { return v.AssociationSize }).(pulumi.IntOutput)
}

// Billing Group ARN
func (o CustomLineItemOutput) BillingGroupArn() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.StringOutput { return v.BillingGroupArn }).(pulumi.StringOutput)
}

func (o CustomLineItemOutput) BillingPeriodRange() CustomLineItemBillingPeriodRangePtrOutput {
	return o.ApplyT(func(v *CustomLineItem) CustomLineItemBillingPeriodRangePtrOutput { return v.BillingPeriodRange }).(CustomLineItemBillingPeriodRangePtrOutput)
}

// Creation timestamp in UNIX epoch time format
func (o CustomLineItemOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.IntOutput { return v.CreationTime }).(pulumi.IntOutput)
}

func (o CustomLineItemOutput) CurrencyCode() CustomLineItemCurrencyCodeOutput {
	return o.ApplyT(func(v *CustomLineItem) CustomLineItemCurrencyCodeOutput { return v.CurrencyCode }).(CustomLineItemCurrencyCodeOutput)
}

func (o CustomLineItemOutput) CustomLineItemChargeDetails() CustomLineItemChargeDetailsPtrOutput {
	return o.ApplyT(func(v *CustomLineItem) CustomLineItemChargeDetailsPtrOutput { return v.CustomLineItemChargeDetails }).(CustomLineItemChargeDetailsPtrOutput)
}

func (o CustomLineItemOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Latest modified timestamp in UNIX epoch time format
func (o CustomLineItemOutput) LastModifiedTime() pulumi.IntOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.IntOutput { return v.LastModifiedTime }).(pulumi.IntOutput)
}

func (o CustomLineItemOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o CustomLineItemOutput) ProductCode() pulumi.StringOutput {
	return o.ApplyT(func(v *CustomLineItem) pulumi.StringOutput { return v.ProductCode }).(pulumi.StringOutput)
}

func (o CustomLineItemOutput) Tags() CustomLineItemTagArrayOutput {
	return o.ApplyT(func(v *CustomLineItem) CustomLineItemTagArrayOutput { return v.Tags }).(CustomLineItemTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CustomLineItemInput)(nil)).Elem(), &CustomLineItem{})
	pulumi.RegisterOutputType(CustomLineItemOutput{})
}
