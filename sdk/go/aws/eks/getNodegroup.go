// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package eks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::EKS::Nodegroup
func LookupNodegroup(ctx *pulumi.Context, args *LookupNodegroupArgs, opts ...pulumi.InvokeOption) (*LookupNodegroupResult, error) {
	var rv LookupNodegroupResult
	err := ctx.Invoke("aws-native:eks:getNodegroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupNodegroupArgs struct {
	Id string `pulumi:"id"`
}

type LookupNodegroupResult struct {
	Arn *string `pulumi:"arn"`
	Id  *string `pulumi:"id"`
	// The Kubernetes labels to be applied to the nodes in the node group when they are created.
	Labels interface{} `pulumi:"labels"`
	// An object representing a node group's launch template specification.
	LaunchTemplate *NodegroupLaunchTemplateSpecification `pulumi:"launchTemplate"`
	// The AMI version of the Amazon EKS-optimized AMI to use with your node group.
	ReleaseVersion *string `pulumi:"releaseVersion"`
	// The scaling configuration details for the Auto Scaling group that is created for your node group.
	ScalingConfig *NodegroupScalingConfig `pulumi:"scalingConfig"`
	// The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.
	Tags interface{} `pulumi:"tags"`
	// The Kubernetes taints to be applied to the nodes in the node group when they are created.
	Taints []NodegroupTaint `pulumi:"taints"`
	// The node group update configuration.
	UpdateConfig *NodegroupUpdateConfig `pulumi:"updateConfig"`
	// The Kubernetes version to use for your managed nodes.
	Version *string `pulumi:"version"`
}

func LookupNodegroupOutput(ctx *pulumi.Context, args LookupNodegroupOutputArgs, opts ...pulumi.InvokeOption) LookupNodegroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNodegroupResult, error) {
			args := v.(LookupNodegroupArgs)
			r, err := LookupNodegroup(ctx, &args, opts...)
			return *r, err
		}).(LookupNodegroupResultOutput)
}

type LookupNodegroupOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupNodegroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNodegroupArgs)(nil)).Elem()
}

type LookupNodegroupResultOutput struct{ *pulumi.OutputState }

func (LookupNodegroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNodegroupResult)(nil)).Elem()
}

func (o LookupNodegroupResultOutput) ToLookupNodegroupResultOutput() LookupNodegroupResultOutput {
	return o
}

func (o LookupNodegroupResultOutput) ToLookupNodegroupResultOutputWithContext(ctx context.Context) LookupNodegroupResultOutput {
	return o
}

func (o LookupNodegroupResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupNodegroupResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The Kubernetes labels to be applied to the nodes in the node group when they are created.
func (o LookupNodegroupResultOutput) Labels() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupNodegroupResult) interface{} { return v.Labels }).(pulumi.AnyOutput)
}

// An object representing a node group's launch template specification.
func (o LookupNodegroupResultOutput) LaunchTemplate() NodegroupLaunchTemplateSpecificationPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *NodegroupLaunchTemplateSpecification { return v.LaunchTemplate }).(NodegroupLaunchTemplateSpecificationPtrOutput)
}

// The AMI version of the Amazon EKS-optimized AMI to use with your node group.
func (o LookupNodegroupResultOutput) ReleaseVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *string { return v.ReleaseVersion }).(pulumi.StringPtrOutput)
}

// The scaling configuration details for the Auto Scaling group that is created for your node group.
func (o LookupNodegroupResultOutput) ScalingConfig() NodegroupScalingConfigPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *NodegroupScalingConfig { return v.ScalingConfig }).(NodegroupScalingConfigPtrOutput)
}

// The metadata, as key-value pairs, to apply to the node group to assist with categorization and organization. Follows same schema as Labels for consistency.
func (o LookupNodegroupResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupNodegroupResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

// The Kubernetes taints to be applied to the nodes in the node group when they are created.
func (o LookupNodegroupResultOutput) Taints() NodegroupTaintArrayOutput {
	return o.ApplyT(func(v LookupNodegroupResult) []NodegroupTaint { return v.Taints }).(NodegroupTaintArrayOutput)
}

// The node group update configuration.
func (o LookupNodegroupResultOutput) UpdateConfig() NodegroupUpdateConfigPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *NodegroupUpdateConfig { return v.UpdateConfig }).(NodegroupUpdateConfigPtrOutput)
}

// The Kubernetes version to use for your managed nodes.
func (o LookupNodegroupResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNodegroupResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNodegroupResultOutput{})
}
