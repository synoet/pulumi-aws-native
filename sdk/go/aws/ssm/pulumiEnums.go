// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ssm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type AssociationComplianceSeverity string

const (
	AssociationComplianceSeverityCritical    = AssociationComplianceSeverity("CRITICAL")
	AssociationComplianceSeverityHigh        = AssociationComplianceSeverity("HIGH")
	AssociationComplianceSeverityMedium      = AssociationComplianceSeverity("MEDIUM")
	AssociationComplianceSeverityLow         = AssociationComplianceSeverity("LOW")
	AssociationComplianceSeverityUnspecified = AssociationComplianceSeverity("UNSPECIFIED")
)

func (AssociationComplianceSeverity) ElementType() reflect.Type {
	return reflect.TypeOf((*AssociationComplianceSeverity)(nil)).Elem()
}

func (e AssociationComplianceSeverity) ToAssociationComplianceSeverityOutput() AssociationComplianceSeverityOutput {
	return pulumi.ToOutput(e).(AssociationComplianceSeverityOutput)
}

func (e AssociationComplianceSeverity) ToAssociationComplianceSeverityOutputWithContext(ctx context.Context) AssociationComplianceSeverityOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AssociationComplianceSeverityOutput)
}

func (e AssociationComplianceSeverity) ToAssociationComplianceSeverityPtrOutput() AssociationComplianceSeverityPtrOutput {
	return e.ToAssociationComplianceSeverityPtrOutputWithContext(context.Background())
}

func (e AssociationComplianceSeverity) ToAssociationComplianceSeverityPtrOutputWithContext(ctx context.Context) AssociationComplianceSeverityPtrOutput {
	return AssociationComplianceSeverity(e).ToAssociationComplianceSeverityOutputWithContext(ctx).ToAssociationComplianceSeverityPtrOutputWithContext(ctx)
}

func (e AssociationComplianceSeverity) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssociationComplianceSeverity) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssociationComplianceSeverity) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AssociationComplianceSeverity) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AssociationComplianceSeverityOutput struct{ *pulumi.OutputState }

func (AssociationComplianceSeverityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssociationComplianceSeverity)(nil)).Elem()
}

func (o AssociationComplianceSeverityOutput) ToAssociationComplianceSeverityOutput() AssociationComplianceSeverityOutput {
	return o
}

func (o AssociationComplianceSeverityOutput) ToAssociationComplianceSeverityOutputWithContext(ctx context.Context) AssociationComplianceSeverityOutput {
	return o
}

func (o AssociationComplianceSeverityOutput) ToAssociationComplianceSeverityPtrOutput() AssociationComplianceSeverityPtrOutput {
	return o.ToAssociationComplianceSeverityPtrOutputWithContext(context.Background())
}

func (o AssociationComplianceSeverityOutput) ToAssociationComplianceSeverityPtrOutputWithContext(ctx context.Context) AssociationComplianceSeverityPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssociationComplianceSeverity) *AssociationComplianceSeverity {
		return &v
	}).(AssociationComplianceSeverityPtrOutput)
}

func (o AssociationComplianceSeverityOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AssociationComplianceSeverityOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssociationComplianceSeverity) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AssociationComplianceSeverityOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssociationComplianceSeverityOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssociationComplianceSeverity) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AssociationComplianceSeverityPtrOutput struct{ *pulumi.OutputState }

func (AssociationComplianceSeverityPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssociationComplianceSeverity)(nil)).Elem()
}

func (o AssociationComplianceSeverityPtrOutput) ToAssociationComplianceSeverityPtrOutput() AssociationComplianceSeverityPtrOutput {
	return o
}

func (o AssociationComplianceSeverityPtrOutput) ToAssociationComplianceSeverityPtrOutputWithContext(ctx context.Context) AssociationComplianceSeverityPtrOutput {
	return o
}

func (o AssociationComplianceSeverityPtrOutput) Elem() AssociationComplianceSeverityOutput {
	return o.ApplyT(func(v *AssociationComplianceSeverity) AssociationComplianceSeverity {
		if v != nil {
			return *v
		}
		var ret AssociationComplianceSeverity
		return ret
	}).(AssociationComplianceSeverityOutput)
}

func (o AssociationComplianceSeverityPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssociationComplianceSeverityPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AssociationComplianceSeverity) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AssociationComplianceSeverityInput is an input type that accepts AssociationComplianceSeverityArgs and AssociationComplianceSeverityOutput values.
// You can construct a concrete instance of `AssociationComplianceSeverityInput` via:
//
//          AssociationComplianceSeverityArgs{...}
type AssociationComplianceSeverityInput interface {
	pulumi.Input

	ToAssociationComplianceSeverityOutput() AssociationComplianceSeverityOutput
	ToAssociationComplianceSeverityOutputWithContext(context.Context) AssociationComplianceSeverityOutput
}

var associationComplianceSeverityPtrType = reflect.TypeOf((**AssociationComplianceSeverity)(nil)).Elem()

type AssociationComplianceSeverityPtrInput interface {
	pulumi.Input

	ToAssociationComplianceSeverityPtrOutput() AssociationComplianceSeverityPtrOutput
	ToAssociationComplianceSeverityPtrOutputWithContext(context.Context) AssociationComplianceSeverityPtrOutput
}

type associationComplianceSeverityPtr string

func AssociationComplianceSeverityPtr(v string) AssociationComplianceSeverityPtrInput {
	return (*associationComplianceSeverityPtr)(&v)
}

func (*associationComplianceSeverityPtr) ElementType() reflect.Type {
	return associationComplianceSeverityPtrType
}

func (in *associationComplianceSeverityPtr) ToAssociationComplianceSeverityPtrOutput() AssociationComplianceSeverityPtrOutput {
	return pulumi.ToOutput(in).(AssociationComplianceSeverityPtrOutput)
}

func (in *associationComplianceSeverityPtr) ToAssociationComplianceSeverityPtrOutputWithContext(ctx context.Context) AssociationComplianceSeverityPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AssociationComplianceSeverityPtrOutput)
}

type AssociationSyncCompliance string

const (
	AssociationSyncComplianceAuto   = AssociationSyncCompliance("AUTO")
	AssociationSyncComplianceManual = AssociationSyncCompliance("MANUAL")
)

func (AssociationSyncCompliance) ElementType() reflect.Type {
	return reflect.TypeOf((*AssociationSyncCompliance)(nil)).Elem()
}

func (e AssociationSyncCompliance) ToAssociationSyncComplianceOutput() AssociationSyncComplianceOutput {
	return pulumi.ToOutput(e).(AssociationSyncComplianceOutput)
}

func (e AssociationSyncCompliance) ToAssociationSyncComplianceOutputWithContext(ctx context.Context) AssociationSyncComplianceOutput {
	return pulumi.ToOutputWithContext(ctx, e).(AssociationSyncComplianceOutput)
}

func (e AssociationSyncCompliance) ToAssociationSyncCompliancePtrOutput() AssociationSyncCompliancePtrOutput {
	return e.ToAssociationSyncCompliancePtrOutputWithContext(context.Background())
}

func (e AssociationSyncCompliance) ToAssociationSyncCompliancePtrOutputWithContext(ctx context.Context) AssociationSyncCompliancePtrOutput {
	return AssociationSyncCompliance(e).ToAssociationSyncComplianceOutputWithContext(ctx).ToAssociationSyncCompliancePtrOutputWithContext(ctx)
}

func (e AssociationSyncCompliance) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssociationSyncCompliance) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e AssociationSyncCompliance) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e AssociationSyncCompliance) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type AssociationSyncComplianceOutput struct{ *pulumi.OutputState }

func (AssociationSyncComplianceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AssociationSyncCompliance)(nil)).Elem()
}

func (o AssociationSyncComplianceOutput) ToAssociationSyncComplianceOutput() AssociationSyncComplianceOutput {
	return o
}

func (o AssociationSyncComplianceOutput) ToAssociationSyncComplianceOutputWithContext(ctx context.Context) AssociationSyncComplianceOutput {
	return o
}

func (o AssociationSyncComplianceOutput) ToAssociationSyncCompliancePtrOutput() AssociationSyncCompliancePtrOutput {
	return o.ToAssociationSyncCompliancePtrOutputWithContext(context.Background())
}

func (o AssociationSyncComplianceOutput) ToAssociationSyncCompliancePtrOutputWithContext(ctx context.Context) AssociationSyncCompliancePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AssociationSyncCompliance) *AssociationSyncCompliance {
		return &v
	}).(AssociationSyncCompliancePtrOutput)
}

func (o AssociationSyncComplianceOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o AssociationSyncComplianceOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssociationSyncCompliance) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o AssociationSyncComplianceOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssociationSyncComplianceOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e AssociationSyncCompliance) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type AssociationSyncCompliancePtrOutput struct{ *pulumi.OutputState }

func (AssociationSyncCompliancePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AssociationSyncCompliance)(nil)).Elem()
}

func (o AssociationSyncCompliancePtrOutput) ToAssociationSyncCompliancePtrOutput() AssociationSyncCompliancePtrOutput {
	return o
}

func (o AssociationSyncCompliancePtrOutput) ToAssociationSyncCompliancePtrOutputWithContext(ctx context.Context) AssociationSyncCompliancePtrOutput {
	return o
}

func (o AssociationSyncCompliancePtrOutput) Elem() AssociationSyncComplianceOutput {
	return o.ApplyT(func(v *AssociationSyncCompliance) AssociationSyncCompliance {
		if v != nil {
			return *v
		}
		var ret AssociationSyncCompliance
		return ret
	}).(AssociationSyncComplianceOutput)
}

func (o AssociationSyncCompliancePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o AssociationSyncCompliancePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *AssociationSyncCompliance) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// AssociationSyncComplianceInput is an input type that accepts AssociationSyncComplianceArgs and AssociationSyncComplianceOutput values.
// You can construct a concrete instance of `AssociationSyncComplianceInput` via:
//
//          AssociationSyncComplianceArgs{...}
type AssociationSyncComplianceInput interface {
	pulumi.Input

	ToAssociationSyncComplianceOutput() AssociationSyncComplianceOutput
	ToAssociationSyncComplianceOutputWithContext(context.Context) AssociationSyncComplianceOutput
}

var associationSyncCompliancePtrType = reflect.TypeOf((**AssociationSyncCompliance)(nil)).Elem()

type AssociationSyncCompliancePtrInput interface {
	pulumi.Input

	ToAssociationSyncCompliancePtrOutput() AssociationSyncCompliancePtrOutput
	ToAssociationSyncCompliancePtrOutputWithContext(context.Context) AssociationSyncCompliancePtrOutput
}

type associationSyncCompliancePtr string

func AssociationSyncCompliancePtr(v string) AssociationSyncCompliancePtrInput {
	return (*associationSyncCompliancePtr)(&v)
}

func (*associationSyncCompliancePtr) ElementType() reflect.Type {
	return associationSyncCompliancePtrType
}

func (in *associationSyncCompliancePtr) ToAssociationSyncCompliancePtrOutput() AssociationSyncCompliancePtrOutput {
	return pulumi.ToOutput(in).(AssociationSyncCompliancePtrOutput)
}

func (in *associationSyncCompliancePtr) ToAssociationSyncCompliancePtrOutputWithContext(ctx context.Context) AssociationSyncCompliancePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(AssociationSyncCompliancePtrOutput)
}

// The key of a key-value pair that identifies the location of an attachment to a document.
type DocumentAttachmentsSourceKey string

const (
	DocumentAttachmentsSourceKeySourceUrl           = DocumentAttachmentsSourceKey("SourceUrl")
	DocumentAttachmentsSourceKeyS3FileUrl           = DocumentAttachmentsSourceKey("S3FileUrl")
	DocumentAttachmentsSourceKeyAttachmentReference = DocumentAttachmentsSourceKey("AttachmentReference")
)

func (DocumentAttachmentsSourceKey) ElementType() reflect.Type {
	return reflect.TypeOf((*DocumentAttachmentsSourceKey)(nil)).Elem()
}

func (e DocumentAttachmentsSourceKey) ToDocumentAttachmentsSourceKeyOutput() DocumentAttachmentsSourceKeyOutput {
	return pulumi.ToOutput(e).(DocumentAttachmentsSourceKeyOutput)
}

func (e DocumentAttachmentsSourceKey) ToDocumentAttachmentsSourceKeyOutputWithContext(ctx context.Context) DocumentAttachmentsSourceKeyOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DocumentAttachmentsSourceKeyOutput)
}

func (e DocumentAttachmentsSourceKey) ToDocumentAttachmentsSourceKeyPtrOutput() DocumentAttachmentsSourceKeyPtrOutput {
	return e.ToDocumentAttachmentsSourceKeyPtrOutputWithContext(context.Background())
}

func (e DocumentAttachmentsSourceKey) ToDocumentAttachmentsSourceKeyPtrOutputWithContext(ctx context.Context) DocumentAttachmentsSourceKeyPtrOutput {
	return DocumentAttachmentsSourceKey(e).ToDocumentAttachmentsSourceKeyOutputWithContext(ctx).ToDocumentAttachmentsSourceKeyPtrOutputWithContext(ctx)
}

func (e DocumentAttachmentsSourceKey) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DocumentAttachmentsSourceKey) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DocumentAttachmentsSourceKey) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DocumentAttachmentsSourceKey) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DocumentAttachmentsSourceKeyOutput struct{ *pulumi.OutputState }

func (DocumentAttachmentsSourceKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DocumentAttachmentsSourceKey)(nil)).Elem()
}

func (o DocumentAttachmentsSourceKeyOutput) ToDocumentAttachmentsSourceKeyOutput() DocumentAttachmentsSourceKeyOutput {
	return o
}

func (o DocumentAttachmentsSourceKeyOutput) ToDocumentAttachmentsSourceKeyOutputWithContext(ctx context.Context) DocumentAttachmentsSourceKeyOutput {
	return o
}

func (o DocumentAttachmentsSourceKeyOutput) ToDocumentAttachmentsSourceKeyPtrOutput() DocumentAttachmentsSourceKeyPtrOutput {
	return o.ToDocumentAttachmentsSourceKeyPtrOutputWithContext(context.Background())
}

func (o DocumentAttachmentsSourceKeyOutput) ToDocumentAttachmentsSourceKeyPtrOutputWithContext(ctx context.Context) DocumentAttachmentsSourceKeyPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DocumentAttachmentsSourceKey) *DocumentAttachmentsSourceKey {
		return &v
	}).(DocumentAttachmentsSourceKeyPtrOutput)
}

func (o DocumentAttachmentsSourceKeyOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DocumentAttachmentsSourceKeyOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DocumentAttachmentsSourceKey) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DocumentAttachmentsSourceKeyOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DocumentAttachmentsSourceKeyOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DocumentAttachmentsSourceKey) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DocumentAttachmentsSourceKeyPtrOutput struct{ *pulumi.OutputState }

func (DocumentAttachmentsSourceKeyPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DocumentAttachmentsSourceKey)(nil)).Elem()
}

func (o DocumentAttachmentsSourceKeyPtrOutput) ToDocumentAttachmentsSourceKeyPtrOutput() DocumentAttachmentsSourceKeyPtrOutput {
	return o
}

func (o DocumentAttachmentsSourceKeyPtrOutput) ToDocumentAttachmentsSourceKeyPtrOutputWithContext(ctx context.Context) DocumentAttachmentsSourceKeyPtrOutput {
	return o
}

func (o DocumentAttachmentsSourceKeyPtrOutput) Elem() DocumentAttachmentsSourceKeyOutput {
	return o.ApplyT(func(v *DocumentAttachmentsSourceKey) DocumentAttachmentsSourceKey {
		if v != nil {
			return *v
		}
		var ret DocumentAttachmentsSourceKey
		return ret
	}).(DocumentAttachmentsSourceKeyOutput)
}

func (o DocumentAttachmentsSourceKeyPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DocumentAttachmentsSourceKeyPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DocumentAttachmentsSourceKey) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DocumentAttachmentsSourceKeyInput is an input type that accepts DocumentAttachmentsSourceKeyArgs and DocumentAttachmentsSourceKeyOutput values.
// You can construct a concrete instance of `DocumentAttachmentsSourceKeyInput` via:
//
//          DocumentAttachmentsSourceKeyArgs{...}
type DocumentAttachmentsSourceKeyInput interface {
	pulumi.Input

	ToDocumentAttachmentsSourceKeyOutput() DocumentAttachmentsSourceKeyOutput
	ToDocumentAttachmentsSourceKeyOutputWithContext(context.Context) DocumentAttachmentsSourceKeyOutput
}

var documentAttachmentsSourceKeyPtrType = reflect.TypeOf((**DocumentAttachmentsSourceKey)(nil)).Elem()

type DocumentAttachmentsSourceKeyPtrInput interface {
	pulumi.Input

	ToDocumentAttachmentsSourceKeyPtrOutput() DocumentAttachmentsSourceKeyPtrOutput
	ToDocumentAttachmentsSourceKeyPtrOutputWithContext(context.Context) DocumentAttachmentsSourceKeyPtrOutput
}

type documentAttachmentsSourceKeyPtr string

func DocumentAttachmentsSourceKeyPtr(v string) DocumentAttachmentsSourceKeyPtrInput {
	return (*documentAttachmentsSourceKeyPtr)(&v)
}

func (*documentAttachmentsSourceKeyPtr) ElementType() reflect.Type {
	return documentAttachmentsSourceKeyPtrType
}

func (in *documentAttachmentsSourceKeyPtr) ToDocumentAttachmentsSourceKeyPtrOutput() DocumentAttachmentsSourceKeyPtrOutput {
	return pulumi.ToOutput(in).(DocumentAttachmentsSourceKeyPtrOutput)
}

func (in *documentAttachmentsSourceKeyPtr) ToDocumentAttachmentsSourceKeyPtrOutputWithContext(ctx context.Context) DocumentAttachmentsSourceKeyPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DocumentAttachmentsSourceKeyPtrOutput)
}

// Specify the document format for the request. The document format can be either JSON or YAML. JSON is the default format.
type DocumentFormat string

const (
	DocumentFormatYaml = DocumentFormat("YAML")
	DocumentFormatJson = DocumentFormat("JSON")
	DocumentFormatText = DocumentFormat("TEXT")
)

func (DocumentFormat) ElementType() reflect.Type {
	return reflect.TypeOf((*DocumentFormat)(nil)).Elem()
}

func (e DocumentFormat) ToDocumentFormatOutput() DocumentFormatOutput {
	return pulumi.ToOutput(e).(DocumentFormatOutput)
}

func (e DocumentFormat) ToDocumentFormatOutputWithContext(ctx context.Context) DocumentFormatOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DocumentFormatOutput)
}

func (e DocumentFormat) ToDocumentFormatPtrOutput() DocumentFormatPtrOutput {
	return e.ToDocumentFormatPtrOutputWithContext(context.Background())
}

func (e DocumentFormat) ToDocumentFormatPtrOutputWithContext(ctx context.Context) DocumentFormatPtrOutput {
	return DocumentFormat(e).ToDocumentFormatOutputWithContext(ctx).ToDocumentFormatPtrOutputWithContext(ctx)
}

func (e DocumentFormat) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DocumentFormat) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DocumentFormat) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DocumentFormat) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DocumentFormatOutput struct{ *pulumi.OutputState }

func (DocumentFormatOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DocumentFormat)(nil)).Elem()
}

func (o DocumentFormatOutput) ToDocumentFormatOutput() DocumentFormatOutput {
	return o
}

func (o DocumentFormatOutput) ToDocumentFormatOutputWithContext(ctx context.Context) DocumentFormatOutput {
	return o
}

func (o DocumentFormatOutput) ToDocumentFormatPtrOutput() DocumentFormatPtrOutput {
	return o.ToDocumentFormatPtrOutputWithContext(context.Background())
}

func (o DocumentFormatOutput) ToDocumentFormatPtrOutputWithContext(ctx context.Context) DocumentFormatPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DocumentFormat) *DocumentFormat {
		return &v
	}).(DocumentFormatPtrOutput)
}

func (o DocumentFormatOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DocumentFormatOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DocumentFormat) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DocumentFormatOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DocumentFormatOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DocumentFormat) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DocumentFormatPtrOutput struct{ *pulumi.OutputState }

func (DocumentFormatPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DocumentFormat)(nil)).Elem()
}

func (o DocumentFormatPtrOutput) ToDocumentFormatPtrOutput() DocumentFormatPtrOutput {
	return o
}

func (o DocumentFormatPtrOutput) ToDocumentFormatPtrOutputWithContext(ctx context.Context) DocumentFormatPtrOutput {
	return o
}

func (o DocumentFormatPtrOutput) Elem() DocumentFormatOutput {
	return o.ApplyT(func(v *DocumentFormat) DocumentFormat {
		if v != nil {
			return *v
		}
		var ret DocumentFormat
		return ret
	}).(DocumentFormatOutput)
}

func (o DocumentFormatPtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DocumentFormatPtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DocumentFormat) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DocumentFormatInput is an input type that accepts DocumentFormatArgs and DocumentFormatOutput values.
// You can construct a concrete instance of `DocumentFormatInput` via:
//
//          DocumentFormatArgs{...}
type DocumentFormatInput interface {
	pulumi.Input

	ToDocumentFormatOutput() DocumentFormatOutput
	ToDocumentFormatOutputWithContext(context.Context) DocumentFormatOutput
}

var documentFormatPtrType = reflect.TypeOf((**DocumentFormat)(nil)).Elem()

type DocumentFormatPtrInput interface {
	pulumi.Input

	ToDocumentFormatPtrOutput() DocumentFormatPtrOutput
	ToDocumentFormatPtrOutputWithContext(context.Context) DocumentFormatPtrOutput
}

type documentFormatPtr string

func DocumentFormatPtr(v string) DocumentFormatPtrInput {
	return (*documentFormatPtr)(&v)
}

func (*documentFormatPtr) ElementType() reflect.Type {
	return documentFormatPtrType
}

func (in *documentFormatPtr) ToDocumentFormatPtrOutput() DocumentFormatPtrOutput {
	return pulumi.ToOutput(in).(DocumentFormatPtrOutput)
}

func (in *documentFormatPtr) ToDocumentFormatPtrOutputWithContext(ctx context.Context) DocumentFormatPtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DocumentFormatPtrOutput)
}

// The type of document to create.
type DocumentType string

const (
	DocumentTypeApplicationConfiguration       = DocumentType("ApplicationConfiguration")
	DocumentTypeApplicationConfigurationSchema = DocumentType("ApplicationConfigurationSchema")
	DocumentTypeAutomation                     = DocumentType("Automation")
	DocumentTypeAutomationChangeTemplate       = DocumentType("Automation.ChangeTemplate")
	DocumentTypeChangeCalendar                 = DocumentType("ChangeCalendar")
	DocumentTypeCloudFormation                 = DocumentType("CloudFormation")
	DocumentTypeCommand                        = DocumentType("Command")
	DocumentTypeDeploymentStrategy             = DocumentType("DeploymentStrategy")
	DocumentTypePackage                        = DocumentType("Package")
	DocumentTypePolicy                         = DocumentType("Policy")
	DocumentTypeProblemAnalysis                = DocumentType("ProblemAnalysis")
	DocumentTypeProblemAnalysisTemplate        = DocumentType("ProblemAnalysisTemplate")
	DocumentTypeSession                        = DocumentType("Session")
)

func (DocumentType) ElementType() reflect.Type {
	return reflect.TypeOf((*DocumentType)(nil)).Elem()
}

func (e DocumentType) ToDocumentTypeOutput() DocumentTypeOutput {
	return pulumi.ToOutput(e).(DocumentTypeOutput)
}

func (e DocumentType) ToDocumentTypeOutputWithContext(ctx context.Context) DocumentTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(DocumentTypeOutput)
}

func (e DocumentType) ToDocumentTypePtrOutput() DocumentTypePtrOutput {
	return e.ToDocumentTypePtrOutputWithContext(context.Background())
}

func (e DocumentType) ToDocumentTypePtrOutputWithContext(ctx context.Context) DocumentTypePtrOutput {
	return DocumentType(e).ToDocumentTypeOutputWithContext(ctx).ToDocumentTypePtrOutputWithContext(ctx)
}

func (e DocumentType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e DocumentType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e DocumentType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e DocumentType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type DocumentTypeOutput struct{ *pulumi.OutputState }

func (DocumentTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DocumentType)(nil)).Elem()
}

func (o DocumentTypeOutput) ToDocumentTypeOutput() DocumentTypeOutput {
	return o
}

func (o DocumentTypeOutput) ToDocumentTypeOutputWithContext(ctx context.Context) DocumentTypeOutput {
	return o
}

func (o DocumentTypeOutput) ToDocumentTypePtrOutput() DocumentTypePtrOutput {
	return o.ToDocumentTypePtrOutputWithContext(context.Background())
}

func (o DocumentTypeOutput) ToDocumentTypePtrOutputWithContext(ctx context.Context) DocumentTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DocumentType) *DocumentType {
		return &v
	}).(DocumentTypePtrOutput)
}

func (o DocumentTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o DocumentTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DocumentType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o DocumentTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DocumentTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e DocumentType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type DocumentTypePtrOutput struct{ *pulumi.OutputState }

func (DocumentTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DocumentType)(nil)).Elem()
}

func (o DocumentTypePtrOutput) ToDocumentTypePtrOutput() DocumentTypePtrOutput {
	return o
}

func (o DocumentTypePtrOutput) ToDocumentTypePtrOutputWithContext(ctx context.Context) DocumentTypePtrOutput {
	return o
}

func (o DocumentTypePtrOutput) Elem() DocumentTypeOutput {
	return o.ApplyT(func(v *DocumentType) DocumentType {
		if v != nil {
			return *v
		}
		var ret DocumentType
		return ret
	}).(DocumentTypeOutput)
}

func (o DocumentTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o DocumentTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *DocumentType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// DocumentTypeInput is an input type that accepts DocumentTypeArgs and DocumentTypeOutput values.
// You can construct a concrete instance of `DocumentTypeInput` via:
//
//          DocumentTypeArgs{...}
type DocumentTypeInput interface {
	pulumi.Input

	ToDocumentTypeOutput() DocumentTypeOutput
	ToDocumentTypeOutputWithContext(context.Context) DocumentTypeOutput
}

var documentTypePtrType = reflect.TypeOf((**DocumentType)(nil)).Elem()

type DocumentTypePtrInput interface {
	pulumi.Input

	ToDocumentTypePtrOutput() DocumentTypePtrOutput
	ToDocumentTypePtrOutputWithContext(context.Context) DocumentTypePtrOutput
}

type documentTypePtr string

func DocumentTypePtr(v string) DocumentTypePtrInput {
	return (*documentTypePtr)(&v)
}

func (*documentTypePtr) ElementType() reflect.Type {
	return documentTypePtrType
}

func (in *documentTypePtr) ToDocumentTypePtrOutput() DocumentTypePtrOutput {
	return pulumi.ToOutput(in).(DocumentTypePtrOutput)
}

func (in *documentTypePtr) ToDocumentTypePtrOutputWithContext(ctx context.Context) DocumentTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(DocumentTypePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(AssociationComplianceSeverityOutput{})
	pulumi.RegisterOutputType(AssociationComplianceSeverityPtrOutput{})
	pulumi.RegisterOutputType(AssociationSyncComplianceOutput{})
	pulumi.RegisterOutputType(AssociationSyncCompliancePtrOutput{})
	pulumi.RegisterOutputType(DocumentAttachmentsSourceKeyOutput{})
	pulumi.RegisterOutputType(DocumentAttachmentsSourceKeyPtrOutput{})
	pulumi.RegisterOutputType(DocumentFormatOutput{})
	pulumi.RegisterOutputType(DocumentFormatPtrOutput{})
	pulumi.RegisterOutputType(DocumentTypeOutput{})
	pulumi.RegisterOutputType(DocumentTypePtrOutput{})
}
