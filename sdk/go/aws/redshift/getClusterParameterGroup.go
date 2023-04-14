// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Redshift::ClusterParameterGroup
func LookupClusterParameterGroup(ctx *pulumi.Context, args *LookupClusterParameterGroupArgs, opts ...pulumi.InvokeOption) (*LookupClusterParameterGroupResult, error) {
	var rv LookupClusterParameterGroupResult
	err := ctx.Invoke("aws-native:redshift:getClusterParameterGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupClusterParameterGroupArgs struct {
	// The name of the cluster parameter group.
	ParameterGroupName string `pulumi:"parameterGroupName"`
}

type LookupClusterParameterGroupResult struct {
	// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
	Parameters []ClusterParameterGroupParameter `pulumi:"parameters"`
}

func LookupClusterParameterGroupOutput(ctx *pulumi.Context, args LookupClusterParameterGroupOutputArgs, opts ...pulumi.InvokeOption) LookupClusterParameterGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupClusterParameterGroupResult, error) {
			args := v.(LookupClusterParameterGroupArgs)
			r, err := LookupClusterParameterGroup(ctx, &args, opts...)
			var s LookupClusterParameterGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupClusterParameterGroupResultOutput)
}

type LookupClusterParameterGroupOutputArgs struct {
	// The name of the cluster parameter group.
	ParameterGroupName pulumi.StringInput `pulumi:"parameterGroupName"`
}

func (LookupClusterParameterGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupClusterParameterGroupArgs)(nil)).Elem()
}

type LookupClusterParameterGroupResultOutput struct{ *pulumi.OutputState }

func (LookupClusterParameterGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupClusterParameterGroupResult)(nil)).Elem()
}

func (o LookupClusterParameterGroupResultOutput) ToLookupClusterParameterGroupResultOutput() LookupClusterParameterGroupResultOutput {
	return o
}

func (o LookupClusterParameterGroupResultOutput) ToLookupClusterParameterGroupResultOutputWithContext(ctx context.Context) LookupClusterParameterGroupResultOutput {
	return o
}

// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
func (o LookupClusterParameterGroupResultOutput) Parameters() ClusterParameterGroupParameterArrayOutput {
	return o.ApplyT(func(v LookupClusterParameterGroupResult) []ClusterParameterGroupParameter { return v.Parameters }).(ClusterParameterGroupParameterArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupClusterParameterGroupResultOutput{})
}
