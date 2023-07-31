// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fsx

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::FSx::DataRepositoryAssociation
func LookupDataRepositoryAssociation(ctx *pulumi.Context, args *LookupDataRepositoryAssociationArgs, opts ...pulumi.InvokeOption) (*LookupDataRepositoryAssociationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataRepositoryAssociationResult
	err := ctx.Invoke("aws-native:fsx:getDataRepositoryAssociation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataRepositoryAssociationArgs struct {
	// The system-generated, unique ID of the data repository association.
	AssociationId string `pulumi:"associationId"`
}

type LookupDataRepositoryAssociationResult struct {
	// The system-generated, unique ID of the data repository association.
	AssociationId *string `pulumi:"associationId"`
	// For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
	ImportedFileChunkSize *int `pulumi:"importedFileChunkSize"`
	// The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.
	ResourceArn *string `pulumi:"resourceArn"`
	// The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
	S3 *DataRepositoryAssociationS3 `pulumi:"s3"`
	// A list of Tag values, with a maximum of 50 elements.
	Tags []DataRepositoryAssociationTag `pulumi:"tags"`
}

func LookupDataRepositoryAssociationOutput(ctx *pulumi.Context, args LookupDataRepositoryAssociationOutputArgs, opts ...pulumi.InvokeOption) LookupDataRepositoryAssociationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataRepositoryAssociationResult, error) {
			args := v.(LookupDataRepositoryAssociationArgs)
			r, err := LookupDataRepositoryAssociation(ctx, &args, opts...)
			var s LookupDataRepositoryAssociationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataRepositoryAssociationResultOutput)
}

type LookupDataRepositoryAssociationOutputArgs struct {
	// The system-generated, unique ID of the data repository association.
	AssociationId pulumi.StringInput `pulumi:"associationId"`
}

func (LookupDataRepositoryAssociationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataRepositoryAssociationArgs)(nil)).Elem()
}

type LookupDataRepositoryAssociationResultOutput struct{ *pulumi.OutputState }

func (LookupDataRepositoryAssociationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataRepositoryAssociationResult)(nil)).Elem()
}

func (o LookupDataRepositoryAssociationResultOutput) ToLookupDataRepositoryAssociationResultOutput() LookupDataRepositoryAssociationResultOutput {
	return o
}

func (o LookupDataRepositoryAssociationResultOutput) ToLookupDataRepositoryAssociationResultOutputWithContext(ctx context.Context) LookupDataRepositoryAssociationResultOutput {
	return o
}

// The system-generated, unique ID of the data repository association.
func (o LookupDataRepositoryAssociationResultOutput) AssociationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataRepositoryAssociationResult) *string { return v.AssociationId }).(pulumi.StringPtrOutput)
}

// For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
func (o LookupDataRepositoryAssociationResultOutput) ImportedFileChunkSize() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupDataRepositoryAssociationResult) *int { return v.ImportedFileChunkSize }).(pulumi.IntPtrOutput)
}

// The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.
func (o LookupDataRepositoryAssociationResultOutput) ResourceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataRepositoryAssociationResult) *string { return v.ResourceArn }).(pulumi.StringPtrOutput)
}

// The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
func (o LookupDataRepositoryAssociationResultOutput) S3() DataRepositoryAssociationS3PtrOutput {
	return o.ApplyT(func(v LookupDataRepositoryAssociationResult) *DataRepositoryAssociationS3 { return v.S3 }).(DataRepositoryAssociationS3PtrOutput)
}

// A list of Tag values, with a maximum of 50 elements.
func (o LookupDataRepositoryAssociationResultOutput) Tags() DataRepositoryAssociationTagArrayOutput {
	return o.ApplyT(func(v LookupDataRepositoryAssociationResult) []DataRepositoryAssociationTag { return v.Tags }).(DataRepositoryAssociationTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataRepositoryAssociationResultOutput{})
}
