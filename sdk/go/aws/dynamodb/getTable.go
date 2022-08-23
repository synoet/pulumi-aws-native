// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dynamodb

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Version: None. Resource Type definition for AWS::DynamoDB::Table
func LookupTable(ctx *pulumi.Context, args *LookupTableArgs, opts ...pulumi.InvokeOption) (*LookupTableResult, error) {
	var rv LookupTableResult
	err := ctx.Invoke("aws-native:dynamodb:getTable", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTableArgs struct {
	TableName string `pulumi:"tableName"`
}

type LookupTableResult struct {
	Arn                              *string                                `pulumi:"arn"`
	AttributeDefinitions             []TableAttributeDefinition             `pulumi:"attributeDefinitions"`
	BillingMode                      *string                                `pulumi:"billingMode"`
	ContributorInsightsSpecification *TableContributorInsightsSpecification `pulumi:"contributorInsightsSpecification"`
	GlobalSecondaryIndexes           []TableGlobalSecondaryIndex            `pulumi:"globalSecondaryIndexes"`
	KeySchema                        interface{}                            `pulumi:"keySchema"`
	KinesisStreamSpecification       *TableKinesisStreamSpecification       `pulumi:"kinesisStreamSpecification"`
	LocalSecondaryIndexes            []TableLocalSecondaryIndex             `pulumi:"localSecondaryIndexes"`
	PointInTimeRecoverySpecification *TablePointInTimeRecoverySpecification `pulumi:"pointInTimeRecoverySpecification"`
	ProvisionedThroughput            *TableProvisionedThroughput            `pulumi:"provisionedThroughput"`
	SSESpecification                 *TableSSESpecification                 `pulumi:"sSESpecification"`
	StreamArn                        *string                                `pulumi:"streamArn"`
	StreamSpecification              *TableStreamSpecification              `pulumi:"streamSpecification"`
	TableClass                       *string                                `pulumi:"tableClass"`
	Tags                             []TableTag                             `pulumi:"tags"`
	TimeToLiveSpecification          *TableTimeToLiveSpecification          `pulumi:"timeToLiveSpecification"`
}

func LookupTableOutput(ctx *pulumi.Context, args LookupTableOutputArgs, opts ...pulumi.InvokeOption) LookupTableResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTableResult, error) {
			args := v.(LookupTableArgs)
			r, err := LookupTable(ctx, &args, opts...)
			var s LookupTableResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTableResultOutput)
}

type LookupTableOutputArgs struct {
	TableName pulumi.StringInput `pulumi:"tableName"`
}

func (LookupTableOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTableArgs)(nil)).Elem()
}

type LookupTableResultOutput struct{ *pulumi.OutputState }

func (LookupTableResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTableResult)(nil)).Elem()
}

func (o LookupTableResultOutput) ToLookupTableResultOutput() LookupTableResultOutput {
	return o
}

func (o LookupTableResultOutput) ToLookupTableResultOutputWithContext(ctx context.Context) LookupTableResultOutput {
	return o
}

func (o LookupTableResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupTableResultOutput) AttributeDefinitions() TableAttributeDefinitionArrayOutput {
	return o.ApplyT(func(v LookupTableResult) []TableAttributeDefinition { return v.AttributeDefinitions }).(TableAttributeDefinitionArrayOutput)
}

func (o LookupTableResultOutput) BillingMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *string { return v.BillingMode }).(pulumi.StringPtrOutput)
}

func (o LookupTableResultOutput) ContributorInsightsSpecification() TableContributorInsightsSpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableContributorInsightsSpecification {
		return v.ContributorInsightsSpecification
	}).(TableContributorInsightsSpecificationPtrOutput)
}

func (o LookupTableResultOutput) GlobalSecondaryIndexes() TableGlobalSecondaryIndexArrayOutput {
	return o.ApplyT(func(v LookupTableResult) []TableGlobalSecondaryIndex { return v.GlobalSecondaryIndexes }).(TableGlobalSecondaryIndexArrayOutput)
}

func (o LookupTableResultOutput) KeySchema() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupTableResult) interface{} { return v.KeySchema }).(pulumi.AnyOutput)
}

func (o LookupTableResultOutput) KinesisStreamSpecification() TableKinesisStreamSpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableKinesisStreamSpecification { return v.KinesisStreamSpecification }).(TableKinesisStreamSpecificationPtrOutput)
}

func (o LookupTableResultOutput) LocalSecondaryIndexes() TableLocalSecondaryIndexArrayOutput {
	return o.ApplyT(func(v LookupTableResult) []TableLocalSecondaryIndex { return v.LocalSecondaryIndexes }).(TableLocalSecondaryIndexArrayOutput)
}

func (o LookupTableResultOutput) PointInTimeRecoverySpecification() TablePointInTimeRecoverySpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TablePointInTimeRecoverySpecification {
		return v.PointInTimeRecoverySpecification
	}).(TablePointInTimeRecoverySpecificationPtrOutput)
}

func (o LookupTableResultOutput) ProvisionedThroughput() TableProvisionedThroughputPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableProvisionedThroughput { return v.ProvisionedThroughput }).(TableProvisionedThroughputPtrOutput)
}

func (o LookupTableResultOutput) SSESpecification() TableSSESpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableSSESpecification { return v.SSESpecification }).(TableSSESpecificationPtrOutput)
}

func (o LookupTableResultOutput) StreamArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *string { return v.StreamArn }).(pulumi.StringPtrOutput)
}

func (o LookupTableResultOutput) StreamSpecification() TableStreamSpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableStreamSpecification { return v.StreamSpecification }).(TableStreamSpecificationPtrOutput)
}

func (o LookupTableResultOutput) TableClass() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *string { return v.TableClass }).(pulumi.StringPtrOutput)
}

func (o LookupTableResultOutput) Tags() TableTagArrayOutput {
	return o.ApplyT(func(v LookupTableResult) []TableTag { return v.Tags }).(TableTagArrayOutput)
}

func (o LookupTableResultOutput) TimeToLiveSpecification() TableTimeToLiveSpecificationPtrOutput {
	return o.ApplyT(func(v LookupTableResult) *TableTimeToLiveSpecification { return v.TimeToLiveSpecification }).(TableTimeToLiveSpecificationPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTableResultOutput{})
}
