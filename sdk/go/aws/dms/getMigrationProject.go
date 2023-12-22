// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dms

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::DMS::MigrationProject
func LookupMigrationProject(ctx *pulumi.Context, args *LookupMigrationProjectArgs, opts ...pulumi.InvokeOption) (*LookupMigrationProjectResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMigrationProjectResult
	err := ctx.Invoke("aws-native:dms:getMigrationProject", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMigrationProjectArgs struct {
	// The property describes an ARN of the migration project.
	MigrationProjectArn string `pulumi:"migrationProjectArn"`
}

type LookupMigrationProjectResult struct {
	// The optional description of the migration project.
	Description *string `pulumi:"description"`
	// The property describes an instance profile arn for the migration project. For read
	InstanceProfileArn *string `pulumi:"instanceProfileArn"`
	// The property describes an instance profile name for the migration project. For read
	InstanceProfileName *string `pulumi:"instanceProfileName"`
	// The property describes an ARN of the migration project.
	MigrationProjectArn *string `pulumi:"migrationProjectArn"`
	// The property describes a creating time of the migration project.
	MigrationProjectCreationTime *string `pulumi:"migrationProjectCreationTime"`
	// The property describes a name to identify the migration project.
	MigrationProjectName *string `pulumi:"migrationProjectName"`
	// The property describes schema conversion application attributes for the migration project.
	SchemaConversionApplicationAttributes *SchemaConversionApplicationAttributesProperties `pulumi:"schemaConversionApplicationAttributes"`
	// The property describes source data provider descriptors for the migration project.
	SourceDataProviderDescriptors []MigrationProjectDataProviderDescriptor `pulumi:"sourceDataProviderDescriptors"`
	// An array of key-value pairs to apply to this resource.
	Tags []MigrationProjectTag `pulumi:"tags"`
	// The property describes target data provider descriptors for the migration project.
	TargetDataProviderDescriptors []MigrationProjectDataProviderDescriptor `pulumi:"targetDataProviderDescriptors"`
	// The property describes transformation rules for the migration project.
	TransformationRules *string `pulumi:"transformationRules"`
}

func LookupMigrationProjectOutput(ctx *pulumi.Context, args LookupMigrationProjectOutputArgs, opts ...pulumi.InvokeOption) LookupMigrationProjectResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMigrationProjectResult, error) {
			args := v.(LookupMigrationProjectArgs)
			r, err := LookupMigrationProject(ctx, &args, opts...)
			var s LookupMigrationProjectResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMigrationProjectResultOutput)
}

type LookupMigrationProjectOutputArgs struct {
	// The property describes an ARN of the migration project.
	MigrationProjectArn pulumi.StringInput `pulumi:"migrationProjectArn"`
}

func (LookupMigrationProjectOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMigrationProjectArgs)(nil)).Elem()
}

type LookupMigrationProjectResultOutput struct{ *pulumi.OutputState }

func (LookupMigrationProjectResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMigrationProjectResult)(nil)).Elem()
}

func (o LookupMigrationProjectResultOutput) ToLookupMigrationProjectResultOutput() LookupMigrationProjectResultOutput {
	return o
}

func (o LookupMigrationProjectResultOutput) ToLookupMigrationProjectResultOutputWithContext(ctx context.Context) LookupMigrationProjectResultOutput {
	return o
}

func (o LookupMigrationProjectResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupMigrationProjectResult] {
	return pulumix.Output[LookupMigrationProjectResult]{
		OutputState: o.OutputState,
	}
}

// The optional description of the migration project.
func (o LookupMigrationProjectResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The property describes an instance profile arn for the migration project. For read
func (o LookupMigrationProjectResultOutput) InstanceProfileArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.InstanceProfileArn }).(pulumi.StringPtrOutput)
}

// The property describes an instance profile name for the migration project. For read
func (o LookupMigrationProjectResultOutput) InstanceProfileName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.InstanceProfileName }).(pulumi.StringPtrOutput)
}

// The property describes an ARN of the migration project.
func (o LookupMigrationProjectResultOutput) MigrationProjectArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.MigrationProjectArn }).(pulumi.StringPtrOutput)
}

// The property describes a creating time of the migration project.
func (o LookupMigrationProjectResultOutput) MigrationProjectCreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.MigrationProjectCreationTime }).(pulumi.StringPtrOutput)
}

// The property describes a name to identify the migration project.
func (o LookupMigrationProjectResultOutput) MigrationProjectName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.MigrationProjectName }).(pulumi.StringPtrOutput)
}

// The property describes schema conversion application attributes for the migration project.
func (o LookupMigrationProjectResultOutput) SchemaConversionApplicationAttributes() SchemaConversionApplicationAttributesPropertiesPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *SchemaConversionApplicationAttributesProperties {
		return v.SchemaConversionApplicationAttributes
	}).(SchemaConversionApplicationAttributesPropertiesPtrOutput)
}

// The property describes source data provider descriptors for the migration project.
func (o LookupMigrationProjectResultOutput) SourceDataProviderDescriptors() MigrationProjectDataProviderDescriptorArrayOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) []MigrationProjectDataProviderDescriptor {
		return v.SourceDataProviderDescriptors
	}).(MigrationProjectDataProviderDescriptorArrayOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupMigrationProjectResultOutput) Tags() MigrationProjectTagArrayOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) []MigrationProjectTag { return v.Tags }).(MigrationProjectTagArrayOutput)
}

// The property describes target data provider descriptors for the migration project.
func (o LookupMigrationProjectResultOutput) TargetDataProviderDescriptors() MigrationProjectDataProviderDescriptorArrayOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) []MigrationProjectDataProviderDescriptor {
		return v.TargetDataProviderDescriptors
	}).(MigrationProjectDataProviderDescriptorArrayOutput)
}

// The property describes transformation rules for the migration project.
func (o LookupMigrationProjectResultOutput) TransformationRules() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMigrationProjectResult) *string { return v.TransformationRules }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMigrationProjectResultOutput{})
}
