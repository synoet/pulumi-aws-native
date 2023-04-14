// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package location

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::Location::GeofenceCollection Resource Type
func LookupGeofenceCollection(ctx *pulumi.Context, args *LookupGeofenceCollectionArgs, opts ...pulumi.InvokeOption) (*LookupGeofenceCollectionResult, error) {
	var rv LookupGeofenceCollectionResult
	err := ctx.Invoke("aws-native:location:getGeofenceCollection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupGeofenceCollectionArgs struct {
	CollectionName string `pulumi:"collectionName"`
}

type LookupGeofenceCollectionResult struct {
	Arn                   *string                        `pulumi:"arn"`
	CollectionArn         *string                        `pulumi:"collectionArn"`
	CreateTime            *string                        `pulumi:"createTime"`
	PricingPlan           *GeofenceCollectionPricingPlan `pulumi:"pricingPlan"`
	PricingPlanDataSource *string                        `pulumi:"pricingPlanDataSource"`
	UpdateTime            *string                        `pulumi:"updateTime"`
}

func LookupGeofenceCollectionOutput(ctx *pulumi.Context, args LookupGeofenceCollectionOutputArgs, opts ...pulumi.InvokeOption) LookupGeofenceCollectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGeofenceCollectionResult, error) {
			args := v.(LookupGeofenceCollectionArgs)
			r, err := LookupGeofenceCollection(ctx, &args, opts...)
			var s LookupGeofenceCollectionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupGeofenceCollectionResultOutput)
}

type LookupGeofenceCollectionOutputArgs struct {
	CollectionName pulumi.StringInput `pulumi:"collectionName"`
}

func (LookupGeofenceCollectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGeofenceCollectionArgs)(nil)).Elem()
}

type LookupGeofenceCollectionResultOutput struct{ *pulumi.OutputState }

func (LookupGeofenceCollectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGeofenceCollectionResult)(nil)).Elem()
}

func (o LookupGeofenceCollectionResultOutput) ToLookupGeofenceCollectionResultOutput() LookupGeofenceCollectionResultOutput {
	return o
}

func (o LookupGeofenceCollectionResultOutput) ToLookupGeofenceCollectionResultOutputWithContext(ctx context.Context) LookupGeofenceCollectionResultOutput {
	return o
}

func (o LookupGeofenceCollectionResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGeofenceCollectionResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupGeofenceCollectionResultOutput) CollectionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGeofenceCollectionResult) *string { return v.CollectionArn }).(pulumi.StringPtrOutput)
}

func (o LookupGeofenceCollectionResultOutput) CreateTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGeofenceCollectionResult) *string { return v.CreateTime }).(pulumi.StringPtrOutput)
}

func (o LookupGeofenceCollectionResultOutput) PricingPlan() GeofenceCollectionPricingPlanPtrOutput {
	return o.ApplyT(func(v LookupGeofenceCollectionResult) *GeofenceCollectionPricingPlan { return v.PricingPlan }).(GeofenceCollectionPricingPlanPtrOutput)
}

func (o LookupGeofenceCollectionResultOutput) PricingPlanDataSource() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGeofenceCollectionResult) *string { return v.PricingPlanDataSource }).(pulumi.StringPtrOutput)
}

func (o LookupGeofenceCollectionResultOutput) UpdateTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupGeofenceCollectionResult) *string { return v.UpdateTime }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGeofenceCollectionResultOutput{})
}
