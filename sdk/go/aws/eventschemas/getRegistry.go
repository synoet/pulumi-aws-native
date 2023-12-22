// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package eventschemas

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EventSchemas::Registry
func LookupRegistry(ctx *pulumi.Context, args *LookupRegistryArgs, opts ...pulumi.InvokeOption) (*LookupRegistryResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRegistryResult
	err := ctx.Invoke("aws-native:eventschemas:getRegistry", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRegistryArgs struct {
	// The ARN of the registry.
	RegistryArn string `pulumi:"registryArn"`
}

type LookupRegistryResult struct {
	// A description of the registry to be created.
	Description *string `pulumi:"description"`
	// The ARN of the registry.
	RegistryArn *string `pulumi:"registryArn"`
	// Tags associated with the resource.
	Tags []RegistryTagsEntry `pulumi:"tags"`
}

func LookupRegistryOutput(ctx *pulumi.Context, args LookupRegistryOutputArgs, opts ...pulumi.InvokeOption) LookupRegistryResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRegistryResult, error) {
			args := v.(LookupRegistryArgs)
			r, err := LookupRegistry(ctx, &args, opts...)
			var s LookupRegistryResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRegistryResultOutput)
}

type LookupRegistryOutputArgs struct {
	// The ARN of the registry.
	RegistryArn pulumi.StringInput `pulumi:"registryArn"`
}

func (LookupRegistryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRegistryArgs)(nil)).Elem()
}

type LookupRegistryResultOutput struct{ *pulumi.OutputState }

func (LookupRegistryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRegistryResult)(nil)).Elem()
}

func (o LookupRegistryResultOutput) ToLookupRegistryResultOutput() LookupRegistryResultOutput {
	return o
}

func (o LookupRegistryResultOutput) ToLookupRegistryResultOutputWithContext(ctx context.Context) LookupRegistryResultOutput {
	return o
}

func (o LookupRegistryResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupRegistryResult] {
	return pulumix.Output[LookupRegistryResult]{
		OutputState: o.OutputState,
	}
}

// A description of the registry to be created.
func (o LookupRegistryResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRegistryResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The ARN of the registry.
func (o LookupRegistryResultOutput) RegistryArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRegistryResult) *string { return v.RegistryArn }).(pulumi.StringPtrOutput)
}

// Tags associated with the resource.
func (o LookupRegistryResultOutput) Tags() RegistryTagsEntryArrayOutput {
	return o.ApplyT(func(v LookupRegistryResult) []RegistryTagsEntry { return v.Tags }).(RegistryTagsEntryArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRegistryResultOutput{})
}
