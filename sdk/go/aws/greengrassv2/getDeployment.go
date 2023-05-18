// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package greengrassv2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource for Greengrass V2 deployment.
func LookupDeployment(ctx *pulumi.Context, args *LookupDeploymentArgs, opts ...pulumi.InvokeOption) (*LookupDeploymentResult, error) {
	var rv LookupDeploymentResult
	err := ctx.Invoke("aws-native:greengrassv2:getDeployment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDeploymentArgs struct {
	DeploymentId string `pulumi:"deploymentId"`
}

type LookupDeploymentResult struct {
	DeploymentId *string     `pulumi:"deploymentId"`
	Tags         interface{} `pulumi:"tags"`
}

func LookupDeploymentOutput(ctx *pulumi.Context, args LookupDeploymentOutputArgs, opts ...pulumi.InvokeOption) LookupDeploymentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDeploymentResult, error) {
			args := v.(LookupDeploymentArgs)
			r, err := LookupDeployment(ctx, &args, opts...)
			var s LookupDeploymentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDeploymentResultOutput)
}

type LookupDeploymentOutputArgs struct {
	DeploymentId pulumi.StringInput `pulumi:"deploymentId"`
}

func (LookupDeploymentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDeploymentArgs)(nil)).Elem()
}

type LookupDeploymentResultOutput struct{ *pulumi.OutputState }

func (LookupDeploymentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDeploymentResult)(nil)).Elem()
}

func (o LookupDeploymentResultOutput) ToLookupDeploymentResultOutput() LookupDeploymentResultOutput {
	return o
}

func (o LookupDeploymentResultOutput) ToLookupDeploymentResultOutputWithContext(ctx context.Context) LookupDeploymentResultOutput {
	return o
}

func (o LookupDeploymentResultOutput) DeploymentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDeploymentResult) *string { return v.DeploymentId }).(pulumi.StringPtrOutput)
}

func (o LookupDeploymentResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupDeploymentResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDeploymentResultOutput{})
}
