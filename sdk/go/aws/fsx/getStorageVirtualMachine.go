// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fsx

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::FSx::StorageVirtualMachine
func LookupStorageVirtualMachine(ctx *pulumi.Context, args *LookupStorageVirtualMachineArgs, opts ...pulumi.InvokeOption) (*LookupStorageVirtualMachineResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupStorageVirtualMachineResult
	err := ctx.Invoke("aws-native:fsx:getStorageVirtualMachine", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStorageVirtualMachineArgs struct {
	StorageVirtualMachineId string `pulumi:"storageVirtualMachineId"`
}

type LookupStorageVirtualMachineResult struct {
	ActiveDirectoryConfiguration *StorageVirtualMachineActiveDirectoryConfiguration `pulumi:"activeDirectoryConfiguration"`
	ResourceArn                  *string                                            `pulumi:"resourceArn"`
	StorageVirtualMachineId      *string                                            `pulumi:"storageVirtualMachineId"`
	SvmAdminPassword             *string                                            `pulumi:"svmAdminPassword"`
	Tags                         []StorageVirtualMachineTag                         `pulumi:"tags"`
	Uuid                         *string                                            `pulumi:"uuid"`
}

func LookupStorageVirtualMachineOutput(ctx *pulumi.Context, args LookupStorageVirtualMachineOutputArgs, opts ...pulumi.InvokeOption) LookupStorageVirtualMachineResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStorageVirtualMachineResult, error) {
			args := v.(LookupStorageVirtualMachineArgs)
			r, err := LookupStorageVirtualMachine(ctx, &args, opts...)
			var s LookupStorageVirtualMachineResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStorageVirtualMachineResultOutput)
}

type LookupStorageVirtualMachineOutputArgs struct {
	StorageVirtualMachineId pulumi.StringInput `pulumi:"storageVirtualMachineId"`
}

func (LookupStorageVirtualMachineOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStorageVirtualMachineArgs)(nil)).Elem()
}

type LookupStorageVirtualMachineResultOutput struct{ *pulumi.OutputState }

func (LookupStorageVirtualMachineResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStorageVirtualMachineResult)(nil)).Elem()
}

func (o LookupStorageVirtualMachineResultOutput) ToLookupStorageVirtualMachineResultOutput() LookupStorageVirtualMachineResultOutput {
	return o
}

func (o LookupStorageVirtualMachineResultOutput) ToLookupStorageVirtualMachineResultOutputWithContext(ctx context.Context) LookupStorageVirtualMachineResultOutput {
	return o
}

func (o LookupStorageVirtualMachineResultOutput) ActiveDirectoryConfiguration() StorageVirtualMachineActiveDirectoryConfigurationPtrOutput {
	return o.ApplyT(func(v LookupStorageVirtualMachineResult) *StorageVirtualMachineActiveDirectoryConfiguration {
		return v.ActiveDirectoryConfiguration
	}).(StorageVirtualMachineActiveDirectoryConfigurationPtrOutput)
}

func (o LookupStorageVirtualMachineResultOutput) ResourceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStorageVirtualMachineResult) *string { return v.ResourceArn }).(pulumi.StringPtrOutput)
}

func (o LookupStorageVirtualMachineResultOutput) StorageVirtualMachineId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStorageVirtualMachineResult) *string { return v.StorageVirtualMachineId }).(pulumi.StringPtrOutput)
}

func (o LookupStorageVirtualMachineResultOutput) SvmAdminPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStorageVirtualMachineResult) *string { return v.SvmAdminPassword }).(pulumi.StringPtrOutput)
}

func (o LookupStorageVirtualMachineResultOutput) Tags() StorageVirtualMachineTagArrayOutput {
	return o.ApplyT(func(v LookupStorageVirtualMachineResult) []StorageVirtualMachineTag { return v.Tags }).(StorageVirtualMachineTagArrayOutput)
}

func (o LookupStorageVirtualMachineResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStorageVirtualMachineResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStorageVirtualMachineResultOutput{})
}
