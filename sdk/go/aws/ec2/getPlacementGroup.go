// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::PlacementGroup
func LookupPlacementGroup(ctx *pulumi.Context, args *LookupPlacementGroupArgs, opts ...pulumi.InvokeOption) (*LookupPlacementGroupResult, error) {
	var rv LookupPlacementGroupResult
	err := ctx.Invoke("aws-native:ec2:getPlacementGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPlacementGroupArgs struct {
	// The Group Name of Placement Group.
	GroupName string `pulumi:"groupName"`
}

type LookupPlacementGroupResult struct {
	// The Group Name of Placement Group.
	GroupName *string `pulumi:"groupName"`
	// An array of key-value pairs to apply to this resource.
	Tags []PlacementGroupTag `pulumi:"tags"`
}

func LookupPlacementGroupOutput(ctx *pulumi.Context, args LookupPlacementGroupOutputArgs, opts ...pulumi.InvokeOption) LookupPlacementGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPlacementGroupResult, error) {
			args := v.(LookupPlacementGroupArgs)
			r, err := LookupPlacementGroup(ctx, &args, opts...)
			var s LookupPlacementGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPlacementGroupResultOutput)
}

type LookupPlacementGroupOutputArgs struct {
	// The Group Name of Placement Group.
	GroupName pulumi.StringInput `pulumi:"groupName"`
}

func (LookupPlacementGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPlacementGroupArgs)(nil)).Elem()
}

type LookupPlacementGroupResultOutput struct{ *pulumi.OutputState }

func (LookupPlacementGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPlacementGroupResult)(nil)).Elem()
}

func (o LookupPlacementGroupResultOutput) ToLookupPlacementGroupResultOutput() LookupPlacementGroupResultOutput {
	return o
}

func (o LookupPlacementGroupResultOutput) ToLookupPlacementGroupResultOutputWithContext(ctx context.Context) LookupPlacementGroupResultOutput {
	return o
}

// The Group Name of Placement Group.
func (o LookupPlacementGroupResultOutput) GroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPlacementGroupResult) *string { return v.GroupName }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupPlacementGroupResultOutput) Tags() PlacementGroupTagArrayOutput {
	return o.ApplyT(func(v LookupPlacementGroupResult) []PlacementGroupTag { return v.Tags }).(PlacementGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPlacementGroupResultOutput{})
}
