// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package imagebuilder

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::ImageBuilder::Image
func LookupImage(ctx *pulumi.Context, args *LookupImageArgs, opts ...pulumi.InvokeOption) (*LookupImageResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupImageResult
	err := ctx.Invoke("aws-native:imagebuilder:getImage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupImageArgs struct {
	// The Amazon Resource Name (ARN) of the image.
	Arn string `pulumi:"arn"`
}

type LookupImageResult struct {
	// The Amazon Resource Name (ARN) of the image.
	Arn *string `pulumi:"arn"`
	// The execution role name/ARN for the image build, if provided
	ExecutionRole *string `pulumi:"executionRole"`
	// The AMI ID of the EC2 AMI in current region.
	ImageId *string `pulumi:"imageId"`
	// URI for containers created in current Region with default ECR image tag
	ImageUri *string `pulumi:"imageUri"`
	// The name of the image.
	Name *string `pulumi:"name"`
}

func LookupImageOutput(ctx *pulumi.Context, args LookupImageOutputArgs, opts ...pulumi.InvokeOption) LookupImageResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupImageResult, error) {
			args := v.(LookupImageArgs)
			r, err := LookupImage(ctx, &args, opts...)
			var s LookupImageResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupImageResultOutput)
}

type LookupImageOutputArgs struct {
	// The Amazon Resource Name (ARN) of the image.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupImageOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupImageArgs)(nil)).Elem()
}

type LookupImageResultOutput struct{ *pulumi.OutputState }

func (LookupImageResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupImageResult)(nil)).Elem()
}

func (o LookupImageResultOutput) ToLookupImageResultOutput() LookupImageResultOutput {
	return o
}

func (o LookupImageResultOutput) ToLookupImageResultOutputWithContext(ctx context.Context) LookupImageResultOutput {
	return o
}

func (o LookupImageResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupImageResult] {
	return pulumix.Output[LookupImageResult]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the image.
func (o LookupImageResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupImageResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The execution role name/ARN for the image build, if provided
func (o LookupImageResultOutput) ExecutionRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupImageResult) *string { return v.ExecutionRole }).(pulumi.StringPtrOutput)
}

// The AMI ID of the EC2 AMI in current region.
func (o LookupImageResultOutput) ImageId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupImageResult) *string { return v.ImageId }).(pulumi.StringPtrOutput)
}

// URI for containers created in current Region with default ECR image tag
func (o LookupImageResultOutput) ImageUri() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupImageResult) *string { return v.ImageUri }).(pulumi.StringPtrOutput)
}

// The name of the image.
func (o LookupImageResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupImageResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupImageResultOutput{})
}
