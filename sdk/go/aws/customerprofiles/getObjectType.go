// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package customerprofiles

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// An ObjectType resource of Amazon Connect Customer Profiles
func LookupObjectType(ctx *pulumi.Context, args *LookupObjectTypeArgs, opts ...pulumi.InvokeOption) (*LookupObjectTypeResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupObjectTypeResult
	err := ctx.Invoke("aws-native:customerprofiles:getObjectType", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupObjectTypeArgs struct {
	// The unique name of the domain.
	DomainName string `pulumi:"domainName"`
	// The name of the profile object type.
	ObjectTypeName string `pulumi:"objectTypeName"`
}

type LookupObjectTypeResult struct {
	// Indicates whether a profile should be created when data is received.
	AllowProfileCreation *bool `pulumi:"allowProfileCreation"`
	// The time of this integration got created.
	CreatedAt *string `pulumi:"createdAt"`
	// Description of the profile object type.
	Description *string `pulumi:"description"`
	// The default encryption key
	EncryptionKey *string `pulumi:"encryptionKey"`
	// The default number of days until the data within the domain expires.
	ExpirationDays *int `pulumi:"expirationDays"`
	// A list of the name and ObjectType field.
	Fields []ObjectTypeFieldMap `pulumi:"fields"`
	// A list of unique keys that can be used to map data to the profile.
	Keys []ObjectTypeKeyMap `pulumi:"keys"`
	// The time of this integration got last updated at.
	LastUpdatedAt *string `pulumi:"lastUpdatedAt"`
	// The format of your sourceLastUpdatedTimestamp that was previously set up.
	SourceLastUpdatedTimestampFormat *string `pulumi:"sourceLastUpdatedTimestampFormat"`
	// The tags (keys and values) associated with the integration.
	Tags []ObjectTypeTag `pulumi:"tags"`
	// A unique identifier for the object template.
	TemplateId *string `pulumi:"templateId"`
}

func LookupObjectTypeOutput(ctx *pulumi.Context, args LookupObjectTypeOutputArgs, opts ...pulumi.InvokeOption) LookupObjectTypeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupObjectTypeResult, error) {
			args := v.(LookupObjectTypeArgs)
			r, err := LookupObjectType(ctx, &args, opts...)
			var s LookupObjectTypeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupObjectTypeResultOutput)
}

type LookupObjectTypeOutputArgs struct {
	// The unique name of the domain.
	DomainName pulumi.StringInput `pulumi:"domainName"`
	// The name of the profile object type.
	ObjectTypeName pulumi.StringInput `pulumi:"objectTypeName"`
}

func (LookupObjectTypeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupObjectTypeArgs)(nil)).Elem()
}

type LookupObjectTypeResultOutput struct{ *pulumi.OutputState }

func (LookupObjectTypeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupObjectTypeResult)(nil)).Elem()
}

func (o LookupObjectTypeResultOutput) ToLookupObjectTypeResultOutput() LookupObjectTypeResultOutput {
	return o
}

func (o LookupObjectTypeResultOutput) ToLookupObjectTypeResultOutputWithContext(ctx context.Context) LookupObjectTypeResultOutput {
	return o
}

func (o LookupObjectTypeResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupObjectTypeResult] {
	return pulumix.Output[LookupObjectTypeResult]{
		OutputState: o.OutputState,
	}
}

// Indicates whether a profile should be created when data is received.
func (o LookupObjectTypeResultOutput) AllowProfileCreation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *bool { return v.AllowProfileCreation }).(pulumi.BoolPtrOutput)
}

// The time of this integration got created.
func (o LookupObjectTypeResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

// Description of the profile object type.
func (o LookupObjectTypeResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The default encryption key
func (o LookupObjectTypeResultOutput) EncryptionKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *string { return v.EncryptionKey }).(pulumi.StringPtrOutput)
}

// The default number of days until the data within the domain expires.
func (o LookupObjectTypeResultOutput) ExpirationDays() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *int { return v.ExpirationDays }).(pulumi.IntPtrOutput)
}

// A list of the name and ObjectType field.
func (o LookupObjectTypeResultOutput) Fields() ObjectTypeFieldMapArrayOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) []ObjectTypeFieldMap { return v.Fields }).(ObjectTypeFieldMapArrayOutput)
}

// A list of unique keys that can be used to map data to the profile.
func (o LookupObjectTypeResultOutput) Keys() ObjectTypeKeyMapArrayOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) []ObjectTypeKeyMap { return v.Keys }).(ObjectTypeKeyMapArrayOutput)
}

// The time of this integration got last updated at.
func (o LookupObjectTypeResultOutput) LastUpdatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *string { return v.LastUpdatedAt }).(pulumi.StringPtrOutput)
}

// The format of your sourceLastUpdatedTimestamp that was previously set up.
func (o LookupObjectTypeResultOutput) SourceLastUpdatedTimestampFormat() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *string { return v.SourceLastUpdatedTimestampFormat }).(pulumi.StringPtrOutput)
}

// The tags (keys and values) associated with the integration.
func (o LookupObjectTypeResultOutput) Tags() ObjectTypeTagArrayOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) []ObjectTypeTag { return v.Tags }).(ObjectTypeTagArrayOutput)
}

// A unique identifier for the object template.
func (o LookupObjectTypeResultOutput) TemplateId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupObjectTypeResult) *string { return v.TemplateId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupObjectTypeResultOutput{})
}
