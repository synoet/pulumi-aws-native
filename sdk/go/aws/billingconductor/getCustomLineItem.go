// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package billingconductor

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A custom line item is an one time charge that is applied to a specific billing group's bill.
func LookupCustomLineItem(ctx *pulumi.Context, args *LookupCustomLineItemArgs, opts ...pulumi.InvokeOption) (*LookupCustomLineItemResult, error) {
	var rv LookupCustomLineItemResult
	err := ctx.Invoke("aws-native:billingconductor:getCustomLineItem", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCustomLineItemArgs struct {
	// ARN
	Arn string `pulumi:"arn"`
}

type LookupCustomLineItemResult struct {
	// ARN
	Arn *string `pulumi:"arn"`
	// Number of source values associated to this custom line item
	AssociationSize    *int                              `pulumi:"associationSize"`
	BillingPeriodRange *CustomLineItemBillingPeriodRange `pulumi:"billingPeriodRange"`
	// Creation timestamp in UNIX epoch time format
	CreationTime                *int                         `pulumi:"creationTime"`
	CurrencyCode                *CustomLineItemCurrencyCode  `pulumi:"currencyCode"`
	CustomLineItemChargeDetails *CustomLineItemChargeDetails `pulumi:"customLineItemChargeDetails"`
	Description                 *string                      `pulumi:"description"`
	// Latest modified timestamp in UNIX epoch time format
	LastModifiedTime *int                `pulumi:"lastModifiedTime"`
	Name             *string             `pulumi:"name"`
	ProductCode      *string             `pulumi:"productCode"`
	Tags             []CustomLineItemTag `pulumi:"tags"`
}

func LookupCustomLineItemOutput(ctx *pulumi.Context, args LookupCustomLineItemOutputArgs, opts ...pulumi.InvokeOption) LookupCustomLineItemResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCustomLineItemResult, error) {
			args := v.(LookupCustomLineItemArgs)
			r, err := LookupCustomLineItem(ctx, &args, opts...)
			var s LookupCustomLineItemResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCustomLineItemResultOutput)
}

type LookupCustomLineItemOutputArgs struct {
	// ARN
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupCustomLineItemOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomLineItemArgs)(nil)).Elem()
}

type LookupCustomLineItemResultOutput struct{ *pulumi.OutputState }

func (LookupCustomLineItemResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCustomLineItemResult)(nil)).Elem()
}

func (o LookupCustomLineItemResultOutput) ToLookupCustomLineItemResultOutput() LookupCustomLineItemResultOutput {
	return o
}

func (o LookupCustomLineItemResultOutput) ToLookupCustomLineItemResultOutputWithContext(ctx context.Context) LookupCustomLineItemResultOutput {
	return o
}

// ARN
func (o LookupCustomLineItemResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Number of source values associated to this custom line item
func (o LookupCustomLineItemResultOutput) AssociationSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *int { return v.AssociationSize }).(pulumi.IntPtrOutput)
}

func (o LookupCustomLineItemResultOutput) BillingPeriodRange() CustomLineItemBillingPeriodRangePtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *CustomLineItemBillingPeriodRange { return v.BillingPeriodRange }).(CustomLineItemBillingPeriodRangePtrOutput)
}

// Creation timestamp in UNIX epoch time format
func (o LookupCustomLineItemResultOutput) CreationTime() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *int { return v.CreationTime }).(pulumi.IntPtrOutput)
}

func (o LookupCustomLineItemResultOutput) CurrencyCode() CustomLineItemCurrencyCodePtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *CustomLineItemCurrencyCode { return v.CurrencyCode }).(CustomLineItemCurrencyCodePtrOutput)
}

func (o LookupCustomLineItemResultOutput) CustomLineItemChargeDetails() CustomLineItemChargeDetailsPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *CustomLineItemChargeDetails { return v.CustomLineItemChargeDetails }).(CustomLineItemChargeDetailsPtrOutput)
}

func (o LookupCustomLineItemResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Latest modified timestamp in UNIX epoch time format
func (o LookupCustomLineItemResultOutput) LastModifiedTime() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *int { return v.LastModifiedTime }).(pulumi.IntPtrOutput)
}

func (o LookupCustomLineItemResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupCustomLineItemResultOutput) ProductCode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) *string { return v.ProductCode }).(pulumi.StringPtrOutput)
}

func (o LookupCustomLineItemResultOutput) Tags() CustomLineItemTagArrayOutput {
	return o.ApplyT(func(v LookupCustomLineItemResult) []CustomLineItemTag { return v.Tags }).(CustomLineItemTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCustomLineItemResultOutput{})
}
